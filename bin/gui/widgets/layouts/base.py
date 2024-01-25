from abc import abstractmethod
from typing import Literal

from PySide6.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QStackedLayout, QVBoxLayout, QWidget


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
        super(BaseLayout, self).__init__(parent=parent)
        self._layout = BaseLayout.layout_types[layout_type]()  # protected
        print(self._layout)

        self.make()
        self.show()
        self.setLayout(self._layout)

    @abstractmethod
    def add_widget(self, widget: QWidget, *args, **kwargs):
        pass

    def set_content_margins(self, left: int, top: int, right: int, bottom: int) -> None:
        self._layout.setContentsMargins(left, top, right, bottom)

    @abstractmethod
    def make(self):
        pass
