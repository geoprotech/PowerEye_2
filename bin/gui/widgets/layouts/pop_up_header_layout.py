from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QPushButton

from .base_horizontal_layout import HorizontalLayout
from bin.gui.widgets.buttons.pop_up_close_button import CloseButtonPopUp
from src.styles.components.widgets.pop_up.object import POP_UP_HEADER_STYLESHEET


class HeaderLayoutPopUp(HorizontalLayout):
    def __init__(self, parent):
        self.parent = parent
        self.title = parent.title_popup
        super().__init__(parent=parent)  # super().__init__ -> -> post_setup -> make -> show

    def make(self) -> None:
        self.setStyleSheet(str(POP_UP_HEADER_STYLESHEET))
        self.setFixedHeight(int(POP_UP_HEADER_STYLESHEET['height']))
        self.setContentsMargins(0, 0, 0, 0)

        text_layout = QLabel(self, text=self.title)
        text_layout.setContentsMargins(0, 0, 0, 0)

        self._buttons_layout = HorizontalLayout(self)
        self._buttons_layout.set_content_margins(0, 0, 0, 0)
        self._buttons_layout.add_widget(CloseButtonPopUp(self, onclick=self.parent.end), alignment=Qt.AlignRight)

        self.add_widget(text_layout, alignment=Qt.AlignLeft)
        self.add_widget(self._buttons_layout)

    def add_button(self, button: QPushButton, stretch: int = 0, alignment: Qt.AlignmentFlag or None = None) -> None:
        self._buttons_layout.add_widget(button, stretch, alignment)
