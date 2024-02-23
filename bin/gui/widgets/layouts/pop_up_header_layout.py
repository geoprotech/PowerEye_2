from .base_horizontal_layout import HorizontalLayout
from src.styles.components.widgets.layouts import HEADER_STYLESHEET


class PopUpHeaderLayout(HorizontalLayout):
    def make(self):
        self.setObjectName("pop_up__header")
        self.setStyleSheet(HEADER_STYLESHEET)
        self.set_content_margins(0, 0, 0, 0)
        self.set_spacing(0)
