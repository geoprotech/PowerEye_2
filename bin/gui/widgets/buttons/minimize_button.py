import PySide6.QtCore as QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

import src.icons as icons
from .base import BaseButton
from bin.storage import Storage
from src.icons import ICONS_PATH
from src.styles.components.widgets.buttons import CLOSE_BUTTON_STYLESHEET, CLOSE_BUTTON_STYLESHEET_HOVER


class MinimizeButton(BaseButton):
    HOVER_ON = CLOSE_BUTTON_STYLESHEET_HOVER
    HOVER_OFF = CLOSE_BUTTON_STYLESHEET

    def __init__(self, parent, window):
        super().__init__(parent=parent, onclick=window.showMinimized)

    def make(self):
        self.setIcon(QIcon(str(ICONS_PATH.joinpath(icons.minimize_button_icon))))
        self.setStyleSheet(str(CLOSE_BUTTON_STYLESHEET))
        width, height = self.size().width(), self.size().height()
        width, height = (int(dimension * 0.1) for dimension in (width, height))
        self.setIconSize(QSize(width, height))
