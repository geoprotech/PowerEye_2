from typing import Union

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from .inner_dim_line_edit import InnerDimLineEdit
from bin.gui.widgets.combobox import DimComboBox
from bin.gui.widgets.labels import DimLabel
from bin.gui.widgets.layouts import HorizontalLayout
from src.styles.components.widgets.line_edit import DIM_LINE_EDIT


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
        self.unit = unit
        self.name_label: Union[DimLabel, None] = None
        self.value_line_edit: Union[InnerDimLineEdit, None] = None
        self.combobox: Union[DimComboBox, None] = None
        self.value = self.unit.value

        super().__init__(parent)

    def make(self):
        self.setObjectName("DimLineEdit")
        self.set_content_margins(5, 0, 5, 0)
        self.set_spacing(5)
        self.name_label = DimLabel(parent=self, text=self.unit.name)
        self.value_line_edit = InnerDimLineEdit(parent=self)
        self.value_line_edit.textChanged.connect(self.on_text_change)
        self.combobox = DimComboBox(parent=self, options=UNITS, on_change=self.convert)
        self.add_widget(self.name_label, alignment=Qt.AlignLeft)
        self.add_widget(self.value_line_edit, alignment=Qt.AlignLeft)
        self.add_widget(self.combobox, alignment=Qt.AlignLeft)
        self.setStyleSheet(DIM_LINE_EDIT)

    def convert(self, new_unit):
        self.unit.convert(self.unit.unit, new_unit)
        self.value_line_edit.setText(str(self.unit.value))

    def on_text_change(self, text):
        try:
            float(text)
            self.unit.value = float(text)
        except ValueError:
            if text:
                self.value_line_edit.setText(str(self.unit.value))
