from abc import abstractmethod
from typing import Callable, Union

from PySide6 import QtCore
from PySide6.QtWidgets import QComboBox, QWidget

from bin.gui.decorators import init_protocol


class BaseComboBox(QComboBox):
    """
    Base abstract class for all buttons.

    methods:
        make(): Function to create button. Must be overwritten.

    """

    storage_signal = QtCore.Signal()

    @init_protocol
    def __init__(self, parent: QWidget, options: list[str], on_change: Union[Callable[[str], None], None] = None):
        super().__init__(parent=parent)
        self.on_choose = on_change
        self.options = options

    def pre_setup(self):
        self.currentTextChanged.connect(self.on_choose)
        self.storage_signal.connect(self.on_emit)
        self.addItems(self.options)

    @abstractmethod
    def make(self):
        """
        Function to create and configure button. Must be overwritten
        """

    @abstractmethod
    def on_emit(self):
        """
        Functon that will be called after storage emit event.
        """
