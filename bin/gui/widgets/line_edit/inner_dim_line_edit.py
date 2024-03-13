from .base import BaseLineEdit
from src.styles.components.widgets.line_edit import INNER_DIM_LINE_EDIT


class InnerDimLineEdit(BaseLineEdit):
    def make(self):
        self.setStyleSheet(INNER_DIM_LINE_EDIT)
