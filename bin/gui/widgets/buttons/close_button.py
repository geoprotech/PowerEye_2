import PySide6.QtCore as QtCore
from PySide6.QtGui import QIcon

import src.icons as icons
from .base import BaseButton
from bin.storage import Storage
from src.icons import ICONS_PATH
from src.styles.components.widgets.buttons import CLOSE_BUTTON_STYLESHEET, CLOSE_BUTTON_STYLESHEET_HOVER


class CloseButton(BaseButton):
    HOVER_ON = CLOSE_BUTTON_STYLESHEET_HOVER
    HOVER_OFF = CLOSE_BUTTON_STYLESHEET

    def __init__(self, parent):
        super().__init__(parent=parent, onclick=QtCore.QCoreApplication.instance().quit)

    def make(self):
        self.setIcon(QIcon(str(ICONS_PATH.joinpath(icons.close_button_icon))))
        self.setStyleSheet(str(CLOSE_BUTTON_STYLESHEET))
        Storage().connect("close_data", self.storage_signal)

    def on_emit(self):
        print(Storage().get("close_data"))
