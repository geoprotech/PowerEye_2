from PySide6.QtWidgets import QDialog

from .base_horizontal_layout import HorizontalLayout
from src.styles.components.widgets.layouts import HEADER_STYLESHEET


class PopUpHeaderLayout(HorizontalLayout):
    def __init__(self, parent: QDialog):
        self.parent = parent
        super().__init__(parent=parent)  # super().__init__ -> -> post_setup -> make -> show

    def make(self):
        self.setObjectName("header")
        self.setStyleSheet(HEADER_STYLESHEET)
        self.set_content_margins(0, 0, 0, 0)
        self.set_spacing(0)
