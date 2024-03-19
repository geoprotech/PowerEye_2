from typing import Union

from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QWidget

from .value_line_edit import ValueLineEdit
from bin.gui.widgets.comboboxes import DimensionalComboBox
from bin.gui.widgets.labels import DimensionalLabel
from bin.gui.widgets.layouts import HorizontalLayout
from src.styles.components.widgets.line_edit import DIMENSIONAL_LINE_EDIT


UNITS = ["m", "cm", "km"]


class TmpUnit:
    def __init__(self):
        self.name = "name"
        self.value = 15
        self.unit = "m"

    def convert(self, init_unit, final_unit):
        self.value *= 2
        self.unit = final_unit


class DimensionalLineEdit(HorizontalLayout):
    def __init__(self, parent: QWidget, unit: TmpUnit):
        self.unit = unit
        self.name_label: Union[DimensionalLabel, None] = None
        self.value_line_edit: Union[ValueLineEdit, None] = None
        self.combobox: Union[DimensionalComboBox, None] = None
        self.value = self.unit.value
        self.is_prev_void = self.value is None
        super().__init__(parent)

    def make(self):
        self.setObjectName("DimLineEdit")
        self.set_content_margins(5, 0, 5, 0)
        self.set_spacing(5)

        self.name_label = DimensionalLabel(parent=self, text=self.unit.name)
        self.value_line_edit = ValueLineEdit(parent=self)
        self.value_line_edit.textChanged.connect(self.on_text_change)

        self.value_line_edit.setValidator(self.__set_up_validator())

        self.combobox = DimensionalComboBox(parent=self, options=UNITS, on_change=self.convert)

        self.add_widget(self.name_label, alignment=Qt.AlignLeft)
        self.add_widget(self.value_line_edit, alignment=Qt.AlignLeft)
        self.add_widget(self.combobox, alignment=Qt.AlignLeft)
        self.setStyleSheet(DIMENSIONAL_LINE_EDIT)

    @staticmethod
    def __set_up_validator() -> QDoubleValidator:
        validator = QDoubleValidator()
        validator.setNotation(QDoubleValidator.StandardNotation)  # noqa
        validator.setRange(-1e6, 1e6)  # Adjust the range as needed
        return validator

    def convert(self, new_unit):
        if self.is_prev_void:
            self.unit.value = 0
        self.unit.convert(self.unit.unit, new_unit)
        if not self.is_prev_void:
            self.value_line_edit.setText(str(self.unit.value))

    def on_text_change(self, text):
        if text:
            self.unit.value = float(text)
            self.is_prev_void = False
        else:
            self.is_prev_void = True
