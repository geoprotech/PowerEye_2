from PySide6.QtWidgets import QLineEdit

from bin.gui.decorators.init_protocol import init_protocol
from src.styles.components.widgets.line_edit import DEFAULT_LINE_EDIT_STYLESHEET


class BaseLineEdit(QLineEdit):
    """
    Base abstract class for all line edit widgets.
        Default stylesheet determined here.

    methods:
        make(): Function to create line edit. Must be overwritten.
        set_tooltip(): Function to set tooltip

    """

    @init_protocol
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

    def make(self):
        self.setStyleSheet(DEFAULT_LINE_EDIT_STYLESHEET)

    def pre_setup(self):
        """
        post setup config
        @return:
        """

    def set_tooltip(self, text: str):
        """
        set tooltip text
        """
        if text:
            self.setToolTip(text)