from .enter_data_input_layout import EnterDataInputLayout
from bin.gui.widgets.layouts import HorizontalLayout, VerticalLayout


class EnterData(VerticalLayout):
    def __init__(self, parent):
        super().__init__(parent)

    def make(self):
        # Line 2:  | label2 | input2 |
        lay2 = HorizontalLayout(self)
        lay2.add_widget(EnterDataInputLayout(self))

        # label2_1 = BaseImageLabel(
        #     lay2, "Ali", pixmap=QPixmap(Path("C:\\Users\\artem\\Desktop\\powereye2\\PowerEye_2\\bin\\ali.png"))
        # )
        # lay2.add_widget(label2_1)

        self.add_widget(lay2)
        self.set_spacing(0)
