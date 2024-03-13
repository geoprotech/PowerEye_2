from .base import BaseLabel
from src.styles.components.widgets.labels import DIM_LABEL_STYLESHEET


class DimLabel(BaseLabel):
    def make(self):
        self.setStyleSheet(DIM_LABEL_STYLESHEET)
