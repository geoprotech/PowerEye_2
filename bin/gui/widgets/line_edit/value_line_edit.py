from .base import BaseLineEdit
from src.styles.components.widgets.line_edit import VALUE_LINE_EDIT


class ValueLineEdit(BaseLineEdit):
    """
    Line edit widget for input widget in dimensional line edit
    """

    def make(self):
        self.setStyleSheet(VALUE_LINE_EDIT)

    def on_emit(self):
        """
        to be overriden later
        @return:
        """
