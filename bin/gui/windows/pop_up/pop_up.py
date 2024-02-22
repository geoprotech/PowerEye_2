from abc import abstractmethod

from base_pop_up import BasePopUP
from PySide6.QtCore import Qt

from bin.gui.widgets.buttons import MaximizeButton, MinimizeButton, PopUpCloseButton
from bin.gui.widgets.layouts import HorizontalLayout


class PopUp(BasePopUP):
    """
    Base class PopUp Window

        Args:
            parent(QWidget): parent
            title(str): Window title in header
    """

    def pre_setup(self) -> None:
        super().pre_setup()
        self._add_title()
        header_control_panel = HorizontalLayout(self)
        header_control_panel.set_content_margins(0, 0, 0, 0)
        header_control_panel.setFixedWidth(120)
        header_control_panel.add_widget(MinimizeButton(header_control_panel, self), alignment=Qt.AlignRight)
        header_control_panel.add_widget(MaximizeButton(header_control_panel, self), alignment=Qt.AlignRight)
        header_control_panel.add_widget(PopUpCloseButton(header_control_panel, self), alignment=Qt.AlignRight)

        self._pop_up_header_layout.add_widget(header_control_panel, alignment=Qt.AlignRight)

    @abstractmethod
    def make(self) -> None:
        """
        Function to create and configure layout. Must be overridden

            Example:
                self.add_widget(Color('red'))
        """
