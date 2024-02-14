from pathlib import Path

from PySide6.QtGui import QPixmap

from bin.gui.widgets.checkboxes import BaseCheckBox
from bin.gui.widgets.labels import BaseImageLabel, BaseLabel
from bin.gui.widgets.layouts import HorizontalLayout, VerticalLayout
from bin.gui.widgets.line_edit import BaseLineEdit


class PlaygroundLayout(VerticalLayout):
    def __init__(self, parent):
        super().__init__(parent)

    def make(self):
        # Line 1 | label1 | input1 |
        lay1 = HorizontalLayout(self)
        label = BaseLabel(parent=self, text="Parameter")
        input1 = BaseLineEdit(self)
        input1.textChanged.connect(lambda text: print(input1.text()))
        checkbox1 = BaseCheckBox(self, "checkbox")
        lay1.add_widget(label)
        lay1.add_widget(input1)
        lay1.add_widget(checkbox1)

        # Line 2:  | label2 | input2 |
        lay2 = HorizontalLayout(self)
        label2 = BaseLabel(parent=self, text="Parameter 2")
        input2 = BaseLineEdit(self)
        input2.textChanged.connect(lambda text: print(input2.text()))
        lay2.add_widget(label2)
        lay2.add_widget(input2)
        label2_1 = BaseImageLabel(
            lay2, "Ali", pixmap=QPixmap(Path("C:\\Users\\artem\\Desktop\\powereye2\\PowerEye_2\\bin\\ali.png"))
        )
        lay2.add_widget(label2_1)

        self.add_widget(lay1)
        self.add_widget(lay2)

        self.setFixedWidth(500)
        self.setFixedHeight(500)
