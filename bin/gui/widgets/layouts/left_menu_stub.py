from .base_vertical_layout import VerticalLayout
from bin.exceptions import LayoutException
from src.styles.components.widgets import LEFT_MENU_STUB_STYLESHEET


class LeftMenuStub(VerticalLayout):
    """
    void stub
    do not add any widgets
    """

    def make(self):
        self.setStyleSheet(LEFT_MENU_STUB_STYLESHEET)

    def add_widget(self, widget):
        raise LayoutException("Do not add widgets to stub")
