from .base import BaseComboBox
from src.styles.components.widgets.comboboxes import DIMENSIONAL_COMBOBOX


class DimensionalComboBox(BaseComboBox):
    def make(self):
        self.setStyleSheet(DIMENSIONAL_COMBOBOX)

    def on_emit(self):
        """
        to be overridden later
        @return:
        """
