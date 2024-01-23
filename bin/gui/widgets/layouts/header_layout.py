from .base_horizontal_layout import HorizontalLayout
from src.styles.components.windows import MAIN_WINDOW_HEADER_STYLESHEET
import bin.gui.widgets.buttons as buttons
import PySide6.QtCore as QtCore


class HeaderLayout(HorizontalLayout):
    def make(self):
        self.setFixedHeight(int(MAIN_WINDOW_HEADER_STYLESHEET["height"]))

        self.setStyleSheet(str(MAIN_WINDOW_HEADER_STYLESHEET))
        self.add_widget(buttons.CloseButton(self), alignment=QtCore.Qt.AlignRight)

