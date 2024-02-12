from bin.gui.widgets.labels import BaseLabel
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
        lay1.add_widget(label)
        lay1.add_widget(input1)

        # Line 2:  | label2 | input2 |
        lay2 = HorizontalLayout(self)
        label2 = BaseLabel(parent=self, text="Parameter 2")
        input2 = BaseLineEdit(self)
        input2.textChanged.connect(lambda text: print(input2.text()))
        lay2.add_widget(label2)
        lay2.add_widget(input2)

        self.add_widget(lay1)
        self.add_widget(lay2)

        self.setFixedWidth(500)
        self.setFixedHeight(500)
