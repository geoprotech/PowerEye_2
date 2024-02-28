from abc import abstractmethod
from typing import Callable

from PySide6 import QtCore
from PySide6.QtWidgets import QPushButton, QWidget

import bin.exceptions as exceptions
from bin.gui import init_protocol
from bin.storage import storage


class BaseButton(QPushButton):
    """
    Base abstract class for all buttons.

    methods:
        make(): Function to create button. Must be overwritten.
        set_tooltip(text)
        add_onclick_event(func)
        delete_onclick_event(event)

    """

    storage_signal = QtCore.Signal()

    @init_protocol
    def __init__(self, parent: QWidget, on_click: Callable or None = None, tooltip: str or None = None):
        super().__init__(parent=parent)
        self.on_click = on_click
        self.tooltip: str = tooltip

    def pre_setup(self):
        self.add_onclick_event(self.on_click)
        self.set_tooltip(self.tooltip)
        self.storage_signal.connect(self.on_emit)

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

    def set_tooltip(self, text: str):
        if text:
            self.setToolTip(text)

    def add_onclick_event(self, func: Callable or None):
        """
        return object, use it to delete onclick event
        """
        if func:
            event = self.clicked.connect(func)
            return event

    def delete_onclick_event(self, event):
        """
        @param event: returned from add_onclick_event
        @return:
        """
        try:
            self.clicked.disconnect(event)
        except RuntimeError:
            raise exceptions.ButtonEventException("wrong onclick event", level=exceptions.ERROR)
