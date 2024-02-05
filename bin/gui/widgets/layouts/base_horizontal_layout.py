from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from .base import BaseLayout


class HorizontalLayout(BaseLayout):
    """
    - Horizontal layout:
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
        super().__init__(parent=parent, layout_type="HBox")

    def make(self):
        """
        Function to create and configure layout. Must be overridden
        """

    def add_widget(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag or None = None) -> None:
        """
        adds a widget to the layout
        @param widget: QWidget
        @param stretch: int
        @param alignment: Qt.AlignmentFlag or None
        @return: None
        """

        # default alignment непонятно как определяется в Qt, поэтому сделал так
        if alignment:
            self._layout.addWidget(widget, stretch, alignment)
        else:
            self._layout.addWidget(widget, stretch)
