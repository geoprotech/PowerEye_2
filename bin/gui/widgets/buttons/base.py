from abc import abstractmethod
from typing import Callable

import PySide6.QtCore as QtCore
from PySide6.QtWidgets import QPushButton, QWidget

import bin.exceptions as exceptions
from bin.gui.decorators import init_protocol
from bin.storage import storage
from src.styles.stylesheet import Stylesheet


@init_protocol
class BaseButton(QPushButton):
    """
    Base abstract class for all buttons.

    attributes:
        HOVER_ON - style for hover. No hover style changes if it's not implemented.
        HOVER_OFF - style for hover exit. You can use default stylesheet for button here.

        FOCUS_ON - style for focus. No focus style if it's not implemented.
        FOCUS_OFF - style for unfocused stated. You can use HOVER_ON stylesheet here.

        TOOLTIP_TEXT - text for tooltip. No tooltip if not implemented.

    methods:
        make(): Function to create button. Must be overwritten.

    """

    storage_signal = QtCore.Signal()

    HOVER_ON: Stylesheet
    HOVER_OFF: Stylesheet

    FOCUS_ON: Stylesheet
    FOCUS_OFF: Stylesheet

    TOOLTIP_TEXT: str

    def __init__(self, parent: QWidget, onclick: Callable or None = None, tooltip: str or None = None):
        super().__init__(parent=parent)
        self.onclick = onclick
        self.tooltip: str = tooltip

    def post_setup(self):
        self.add_onclick_event(self.onclick)
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

    def enterEvent(self, event):  # noqa
        if hasattr(self, "HOVER_ON"):
            self.setStyleSheet(str(self.HOVER_ON))
        return super().enterEvent(event)

    def leaveEvent(self, event):  # noqa
        if hasattr(self, "HOVER_OFF"):
            self.setStyleSheet(str(self.HOVER_OFF))
        return super().leaveEvent(event)

    def focusInEvent(self, event):  # noqa
        if hasattr(self, "FOCUS_ON"):
            self.setStyleSheet(str(self.FOCUS_ON))
        return super().focusInEvent(event)

    def focusOutEvent(self, event):  # noqa
        if hasattr(self, "FOCUS_OFF"):
            self.setStyleSheet(str(self.FOCUS_OFF))
        return super().focusOutEvent(event)

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
