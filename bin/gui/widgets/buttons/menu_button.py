from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from .base import BaseButton
from src.icons import ICONS_PATH
from src.styles.components.widgets.buttons import LEFT_MENU_BUTTON_STYLESHEET, LEFT_MENU_BUTTON_STYLESHEET_HOVER


class MenuButton(BaseButton):
    HOVER_ON = LEFT_MENU_BUTTON_STYLESHEET_HOVER
    HOVER_OFF = LEFT_MENU_BUTTON_STYLESHEET

    def __init__(self, parent):
        super().__init__(parent=parent)

    def make(self):
        self.setIcon(QIcon(str(ICONS_PATH.joinpath("menu_lines.png"))))
        self.setStyleSheet(str(LEFT_MENU_BUTTON_STYLESHEET))
        size = self.size()
        icon_width = int(size.width() * 0.8)
        icon_height = int(size.height() * 0.8)
        self.setIconSize(QSize(icon_width, icon_height))
