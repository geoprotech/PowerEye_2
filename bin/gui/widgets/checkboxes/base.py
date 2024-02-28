from abc import abstractmethod
from typing import Callable

from PySide6.QtWidgets import QCheckBox, QWidget

import bin.exceptions as exceptions
from bin.gui import init_protocol
from src.styles.components.widgets.checkboxes import DEFAULT_CHECKBOX_STYLESHEET


class BaseCheckbox(QCheckBox):
    """
    Base abstract class for all custom checkboxes.

    methods:
        make(): Function to create checkbox. Must be overwritten.

    """

    @init_protocol
    def __init__(self, parent: QWidget, text: str, on_change: Callable or None = None, tooltip: str or None = None):
        super().__init__(parent=parent, text=text)
        self.on_change = on_change
        self.tooltip: str = tooltip

    def pre_setup(self):
        self.add_on_state_changed_event(self.on_change)
        self.set_tooltip(self.tooltip)
        self.setStyleSheet(DEFAULT_CHECKBOX_STYLESHEET)

    @abstractmethod
    def make(self):
        """
        Function to create and configure checkboxes. Must be overwritten
        @return:
        """

    def set_tooltip(self, text: str):
        if text:
            self.setToolTip(text)

    def add_on_state_changed_event(self, func: Callable or None):
        """
        return object, use it to delete on_state_changed event
        """
        if func:
            event = self.stateChanged.connect(func)
            return event

    def delete_on_state_changed_event(self, event):
        """
        @param event: returned from add_on_state_changed_event
        @return:
        """
        try:
            self.stateChanged.disconnect(event)
        except RuntimeError:
            raise exceptions.CheckboxEventException("wrong on_state_changed event", level=exceptions.ERROR)
