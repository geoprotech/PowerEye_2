from abc import abstractmethod

from PySide6 import QtCore
from PySide6.QtWidgets import QLineEdit

from bin.gui.decorators import init_protocol
from src.styles.components.widgets.line_edit import DEFAULT_LINE_EDIT_STYLESHEET


class BaseLineEdit(QLineEdit):
    """
    Base abstract class for all line edit widgets.
        Default stylesheet determined here.

    methods:
        make(): Function to create line edit. Must be overwritten.
        set_tooltip(): Function to set tooltip

    """

    storage_signal = QtCore.Signal()

    @init_protocol
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    @abstractmethod
    def make(self):
        """
        to be overridden
        """

    @abstractmethod
    def on_emit(self):
        """
        Functon that will be called after storage emit event.
        """

    def pre_setup(self):
        """
        post setup config
        @return:
        """
        self.setStyleSheet(DEFAULT_LINE_EDIT_STYLESHEET)
        self.storage_signal.connect(self.on_emit)

    def set_tooltip(self, text: str):
        """
        set tooltip text
        """
        if text:
            self.setToolTip(text)
