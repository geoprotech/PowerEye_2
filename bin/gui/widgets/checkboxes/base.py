from abc import abstractmethod
from typing import Callable

from PySide6.QtWidgets import QCheckBox, QStyle, QWidget

from src.styles.components.widgets.checkboxes import CHECKBOX_STYLESHEET


class BaseCheckBox(QCheckBox):
    """
    Base abstract class for all custom checkboxes.

    methods:
        make(): Function to create checkbox. Must be overwritten.

    """

    def __init__(
        self, parent: QWidget, text: str, on_state_changed: Callable or None = None, tooltip: str or None = None
    ):
        super().__init__(parent=parent, text=text)
        self.on_state_changed = on_state_changed
        self.tooltip: str = tooltip
        self.post_setup()

    def post_setup(self):
        self.add_on_state_changed_event(self.on_state_changed)
        self.set_tooltip(self.tooltip)
        self.make()
        self.show()

    @abstractmethod
    def make(self):
        self.setStyleSheet(CHECKBOX_STYLESHEET)

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
            pass
            # raise exceptions.CheckboxEventException("wrong on_state_changed event", level=exceptions.ERROR)

    def initStyleOption(self, option):  # noqa
        super().initStyleOption(option)
        if self.isChecked():
            option.state |= QStyle.State_On
        else:
            option.state |= QStyle.State_Off
