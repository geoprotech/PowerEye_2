import PySide6.QtCore as QtCore

import bin.gui.widgets.buttons as buttons
from .base_horizontal_layout import HorizontalLayout
from src.styles.components.windows import MAIN_WINDOW_HEADER_STYLESHEET


class HeaderLayout(HorizontalLayout):
    """
    Header layout for application header
    """

    def make(self):
        self.setFixedHeight(int(MAIN_WINDOW_HEADER_STYLESHEET["height"]))
        self.setStyleSheet(str(MAIN_WINDOW_HEADER_STYLESHEET))

        logo_layout = HorizontalLayout(self)
        buttons_layout = HorizontalLayout(self)
        buttons_layout.setFixedWidth(100)
        buttons_layout.add_widget(buttons.CloseButton(self), alignment=QtCore.Qt.AlignRight)
        buttons_layout.add_widget(buttons.CloseButton(self), alignment=QtCore.Qt.AlignRight)
        buttons_layout.add_widget(buttons.CloseButton(self), alignment=QtCore.Qt.AlignRight)

        self.add_widget(logo_layout)
        self.add_widget(buttons_layout)
        # self.add_widget(buttons.CloseButton(self), alignment=QtCore.Qt.AlignRight)
