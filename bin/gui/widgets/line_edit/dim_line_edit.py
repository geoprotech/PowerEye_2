from PySide6.QtWidgets import QWidget

from bin.gui.widgets import BaseLabel, BaseLineEdit, HorizontalLayout


UNITS = ["m", "cm", "km"]


class TmpUnit:
    def __init__(self):
        self.name = "name"
        self.value = 15
        self.unit = "m"

    def convert(self, init_unit, final_unit):
        self.value *= 2
        self.unit = final_unit


class DimLineEdit(HorizontalLayout):
    def __init__(self, parent: QWidget, unit: TmpUnit):
        super().__init__(parent)
        self.unit = unit
        self.name_label = BaseLabel(parent=self, text=self.unit.name)
        self.value_line_edit = BaseLineEdit(parent=self)
