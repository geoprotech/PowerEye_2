from bin.gui.widgets.layouts import HorizontalLayout, VerticalLayout
from bin.gui.widgets.line_edit import DimensionalLineEdit, TmpUnit


class EnterDataInputLayout(VerticalLayout):
    def __init__(self, parent):
        super().__init__(parent)

    def make(self):
        self.__fill_data()
        self.setFixedWidth(1000)

    def __fill_data(self):
        for i in range(5):
            tmp_layout = HorizontalLayout(self)
            tmp_layout.add_widget(DimensionalLineEdit(parent=self, unit=TmpUnit()))
            tmp_layout.add_widget(DimensionalLineEdit(parent=self, unit=TmpUnit()))
            self.add_widget(tmp_layout)
