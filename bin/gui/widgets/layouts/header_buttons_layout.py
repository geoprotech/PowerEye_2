from PySide6 import QtCore

import bin.gui.widgets.buttons as buttons
from bin.gui.widgets.layouts import HorizontalLayout
from bin.storage import Storage
from src.styles.components.widgets import HEADER_BUTTONS_LAYOUT_STYLESHEET


class HeaderButtonsLayout(HorizontalLayout):
    def make(self):
        self.setObjectName("header_buttons_layout")
        self.setStyleSheet(HEADER_BUTTONS_LAYOUT_STYLESHEET)
        self.setFixedWidth(120)
        self.set_content_margins(0, 0, 0, 0)
        self.set_spacing(0)

        window = Storage().get("main_window")

        self.add_widget(buttons.MinimizeButton(self, window), alignment=QtCore.Qt.AlignRight)  # noqa
        self.add_widget(buttons.MaximizeButton(self, window), alignment=QtCore.Qt.AlignRight)  # noqa
        self.add_widget(buttons.CloseButton(self), alignment=QtCore.Qt.AlignRight)  # noqa
