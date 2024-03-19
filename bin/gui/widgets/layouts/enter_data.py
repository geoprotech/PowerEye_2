from .enter_data_input_layout import EnterDataInputLayout
from bin.gui.widgets.layouts import HorizontalLayout, VerticalLayout


class EnterData(VerticalLayout):
    def __init__(self, parent):
        super().__init__(parent)

    def make(self):
        lay2 = HorizontalLayout(self)
        lay2.add_widget(EnterDataInputLayout(self))

        self.add_widget(lay2)
        self.set_spacing(0)
