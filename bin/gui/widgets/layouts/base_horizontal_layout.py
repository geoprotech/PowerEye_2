from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from .base import BaseLayout


class HorizontalLayout(BaseLayout):
    def __init__(self, parent: QWidget):
        super().__init__(parent=parent, layout_type="HBox")

    def add_widget(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag = Qt.AlignCenter) -> None:
        self._layout.addWidget(widget, stretch, alignment)

    def make(self):
        pass
