from abc import abstractmethod
from typing import Literal

from PySide6 import QtCore
from PySide6.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QStackedLayout, QVBoxLayout, QWidget

from bin.gui.decorators import init_protocol


class BaseLayout(QFrame):
    """
    layout_types:
        "HBox" - horizontal layout
        "VBox" - vertical layout
        "Grid" - grid layout
        "Stacked" - stacked layout
    """

    storage_signal = QtCore.Signal()
    layout_types = {"HBox": QHBoxLayout, "VBox": QVBoxLayout, "Grid": QGridLayout, "Stacked": QStackedLayout}

    @init_protocol
    def __init__(self, parent: QWidget, layout_type: Literal["HBox", "VBox", "Grid", "Stacked"]):
        super().__init__(parent=parent)
        self._layout = BaseLayout.layout_types.get(layout_type)()  # protected

    @abstractmethod
    def add_widget(self, widget: QWidget, *args, **kwargs):
        pass

    @abstractmethod
    def make(self):
        """
        Function to create and config the layout. Must be overriden
        """

    @abstractmethod
    def on_emit(self):
        """
        Functon that will be called after storage emit event.
        """

    def pre_setup(self):
        self.setLayout(self._layout)
        self.storage_signal.connect(self.on_emit)
        # self.set_content_margins(0,0,0,0)
        # self.set_spacing(0)

    def set_content_margins(self, left: int, top: int, right: int, bottom: int) -> None:
        self._layout.setContentsMargins(left, top, right, bottom)

    def set_spacing(self, spacing: int) -> None:
        self._layout.setSpacing(spacing)
