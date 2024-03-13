from .base import BaseComboBox
from src.styles.components.widgets.combo_boxes import DIM_COMBO_BOX


class DimComboBox(BaseComboBox):
    def make(self):
        self.setStyleSheet(DIM_COMBO_BOX)
