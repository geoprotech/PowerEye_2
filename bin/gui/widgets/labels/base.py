from abc import abstractmethod

from PySide6 import QtCore
from PySide6.QtWidgets import QLabel

from bin.gui.decorators import init_protocol
from src.styles.components.widgets.labels import DEFAULT_LABEL_STYLESHEET


class BaseLabel(QLabel):
    """
    Base abstract class for all labels.
    Default stylesheet determined here.


    methods:
        make(): Function to create label. Must be overwritten.
        set_tooltip(): Function to set tooltip
    """

    storage_signal = QtCore.Signal()

    @init_protocol
    def __init__(self, parent, text: str or None = None, *args, **kwargs):
        super().__init__(parent=parent, text=text, *args, **kwargs)

    @abstractmethod
    def make(self):
        """
        determ default stylesheet
        """

    @abstractmethod
    def on_emit(self):
        """
        Functon that will be called after storage emit event.
        """

    def pre_setup(self):
        self.setStyleSheet(str(DEFAULT_LABEL_STYLESHEET))
        self.storage_signal.connect(self.on_emit)
