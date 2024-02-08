from abc import abstractmethod

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QWidget

from bin.gui.decorators import init_protocol
from bin.gui.widgets.layouts import HeaderLayoutPopUp, VerticalLayout


@init_protocol
class PopUp(QDialog):
    """
    Base class PopUp Window

        Args:
            parent(QWidget): parent
            title_popup(str): Window title in header
            size(tuple(x: int, y: int,  width: int, height: int)): PopUP size options
    """

    def __init__(self, parent: QWidget, title: str, size: tuple):
        self.title_popup = title
        self.size = size
        super().__init__(parent=parent)

    def post_setup(self) -> None:
        self.move(*self.size[:2])
        self.resize(*self.size[2:])
        self.setWindowFlag(Qt.FramelessWindowHint)

        self._layout_main = QVBoxLayout()
        self._layout_main.setContentsMargins(0, 0, 0, 0)

        self._layout = VerticalLayout(parent=self)
        self._layout.set_content_margins(0, 0, 0, 0)

        self.headerlayoutPopUp = HeaderLayoutPopUp(parent=self)
        self._layout.add_widget(self.headerlayoutPopUp)

        self._layout_main.addWidget(self._layout)
        self.setLayout(self._layout_main)

    @abstractmethod
    def make(self) -> None:
        """
        Basic window designer

            Example:
                self._add_widget(Color('red'))
                button = CloseButtonPopUp(self.headerlayoutPopUp, onclick=self.end)
                self._add_control_buttons(button, alignment=Qt.AlignRight)
        """

    def _add_widget(self, widget: QWidget) -> None:
        self._layout.add_widget(widget)

    def _add_control_buttons(
        self, button: QPushButton, stretch: int = 0, alignment: Qt.AlignmentFlag or None = None
    ) -> None:
        self.headerlayoutPopUp.add_button(button, stretch, alignment)

    def _add_widget_header(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag or None = None) -> None:
        self.headerlayoutPopUp.add_widget(widget, stretch, alignment)

    def show(self):
        self.exec()

    def end(self) -> None:
        """
        Closing a PopUP
        """
        self.accept()
