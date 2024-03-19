from .base import BaseLabel
from src.styles.components.widgets.labels import DIMENSIONAL_LABEL_STYLESHEET


class DimensionalLabel(BaseLabel):
    def make(self):
        self.setStyleSheet(DIMENSIONAL_LABEL_STYLESHEET)

    def on_emit(self):
        """
        to be overridden later
        @return:
        """
