from PySide6.QtGui import QPixmap

from bin.gui.widgets.checkboxes import BaseCheckbox
from bin.gui.widgets.comboboxes import DimensionalComboBox
from bin.gui.widgets.labels import BaseLabel, ImageLabel
from bin.gui.widgets.layouts import HorizontalLayout, VerticalLayout
from bin.gui.widgets.line_edit import BaseLineEdit, DimensionalLineEdit, TmpUnit
from bin.gui.widgets.radiobuttons import BaseRadioButton
from src.icons import skyrus_logo


class PlaygroundLayout(VerticalLayout):
    def __init__(self, parent):
        super().__init__(parent)

    def make(self):
        self.setStyleSheet("background-color: white")
        # Line 1 | label1 | input1 |
        lay1 = HorizontalLayout(self)
        label = BaseLabel(parent=self, text="Parameter")
        input1 = BaseLineEdit(self)
        input1.textChanged.connect(lambda text: print(input1.text()))
        checkbox1 = BaseCheckbox(self, "checkbox")
        radio1 = BaseRadioButton(self, text="option1")

        lay1.add_widget(label)
        lay1.add_widget(input1)
        lay1.add_widget(checkbox1)
        lay1.add_widget(radio1)
        radio1.clicked.connect(lambda checked: print(checked))

        # Line 2:  | label2 | input2 |
        lay2 = HorizontalLayout(self)
        label2 = BaseLabel(parent=self, text="Parameter 2")
        input2 = BaseLineEdit(self)
        input2.textChanged.connect(lambda text: print(input2.text()))
        radio2 = BaseRadioButton(self, text="option1")
        image = ImageLabel(parent=self, pixmap=QPixmap(skyrus_logo))
        lay2.add_widget(label2)
        lay2.add_widget(input2)
        lay2.add_widget(radio2)
        lay2.add_widget(image)
        lay2.add_widget(
            DimensionalComboBox(parent=self, options=["Option 1", "Option 2", "Option3"], on_change=lambda x: print(x))
        )
        lay2.add_widget(DimensionalLineEdit(parent=self, unit=TmpUnit()))
        radio2.clicked.connect(lambda checked: print(checked))

        # label2_1 = BaseImageLabel(
        #     lay2, "Ali", pixmap=QPixmap(Path("C:\\Users\\artem\\Desktop\\powereye2\\PowerEye_2\\bin\\ali.png"))
        # )
        # lay2.add_widget(label2_1)

        self.add_widget(lay1)
        self.add_widget(lay2)

        self.setFixedWidth(800)
        self.setFixedHeight(400)
