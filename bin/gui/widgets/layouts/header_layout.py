import PySide6.QtCore as QtCore

import bin.gui.widgets.buttons as buttons
from .base_horizontal_layout import HorizontalLayout
from bin.storage import Storage
from src.styles.components.windows import MAIN_WINDOW_HEADER_STYLESHEET


class HeaderLayout(HorizontalLayout):
    """
    Header layout for application header
    """

    def make(self):
        self.setFixedHeight(int(MAIN_WINDOW_HEADER_STYLESHEET["height"]))
        self.setStyleSheet(str(MAIN_WINDOW_HEADER_STYLESHEET))
        self.set_content_margins(0, 0, 0, 0)
        self.set_spacing(0)

        logo_layout = HorizontalLayout(self)
        buttons_layout = HorizontalLayout(self)
        buttons_layout.setFixedWidth(120)
        buttons_layout.set_content_margins(0, 0, 0, 0)
        buttons_layout.set_spacing(0)
        window = Storage().get_data("main_window")
        buttons_layout.add_widget(buttons.MinimizeButton(self, window), alignment=QtCore.Qt.AlignRight)
        buttons_layout.add_widget(buttons.MaximizeButton(self, window), alignment=QtCore.Qt.AlignRight)
        buttons_layout.add_widget(buttons.CloseButton(self), alignment=QtCore.Qt.AlignRight)

        self.add_widget(logo_layout)
        self.add_widget(buttons_layout)
