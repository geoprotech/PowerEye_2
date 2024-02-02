from abc import abstractmethod
from typing import Literal

from PySide6.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QStackedLayout, QVBoxLayout, QWidget

from bin.gui.decorators import init_protocol


@init_protocol
class BaseLayout(QFrame):
    """
    layout_types:
        "HBox" - horizontal layout
        "VBox" - vertical layout
        "Grid" - grid layout
        "Stacked" - stacked layout
    """

    layout_types = {"HBox": QHBoxLayout, "VBox": QVBoxLayout, "Grid": QGridLayout, "Stacked": QStackedLayout}

    def __init__(self, parent: QWidget, layout_type: Literal["HBox", "VBox", "Grid", "Stacked"]):
        super().__init__(parent=parent)
        self._layout = BaseLayout.layout_types.get(layout_type)()  # protected

    def post_setup(self):
        self.setLayout(self._layout)

    @abstractmethod
    def add_widget(self, widget: QWidget, *args, **kwargs):
        pass

    @abstractmethod
    def make(self):
        """
        Function to create and config the layout. Must be overriden
        """

    def set_content_margins(self, left: int, top: int, right: int, bottom: int) -> None:
        self._layout.setContentsMargins(left, top, right, bottom)
