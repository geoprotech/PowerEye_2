from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from .base import BaseLayout


class VerticalLayout(BaseLayout):
    """
    - Vertical layout:
    - Inheritance order:
        QFrame -> BaseLayout -> HorizontalLayout
    Public methods:
        - add_widget
        - set_content_margins
        - same as in QFrame
    Public fields:
        - same as in QFrame
    """

    def __init__(self, parent: QWidget):
        super().__init__(parent=parent, layout_type="VBox")

    def add_widget(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag | None = None) -> None:
        """
        adds a widget to the layout
        @param widget: QWidget
        @param stretch: int
        @param alignment: Qt.AlignmentFlag or None
        @return: None
        """
        if alignment:
            self._layout.addWidget(widget, stretch, alignment)
        else:
            self._layout.addWidget(widget, stretch=stretch)

    def make(self):
        pass
