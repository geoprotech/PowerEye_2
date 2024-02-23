from abc import abstractmethod

from PySide6.QtCore import Qt

from .base_popup import BasePopUp
from bin.gui.widgets.buttons import MaximizeButton, MinimizeButton
from bin.gui.widgets.layouts import HorizontalLayout
from bin.gui.windows.pop_up.buttons_popup import CloseButtonPopUp


# from bin.gui.widgets.stub import Color


class PopUp(BasePopUp):
    """
    Base class PopUp Window

        Args:
            parent(QWidget): parent
            title(str): Window title in header
    """

    def pre_setup(self) -> None:
        super().pre_setup()
        header_control_panel = HorizontalLayout(self)
        header_control_panel.set_content_margins(0, 0, 0, 0)
        header_control_panel.setFixedWidth(120)
        header_control_panel.add_widget(MinimizeButton(header_control_panel, self), alignment=Qt.AlignRight)
        header_control_panel.add_widget(MaximizeButton(header_control_panel, self), alignment=Qt.AlignRight)
        header_control_panel.add_widget(CloseButtonPopUp(header_control_panel, self), alignment=Qt.AlignRight)

        self._header_layout_popup.add_widget(header_control_panel, alignment=Qt.AlignRight)

    @abstractmethod
    def make(self) -> None:
        """
        Function to create and configure layout. Must be overridden

            Example:
                self.add_widget(Color('red'))
        """
