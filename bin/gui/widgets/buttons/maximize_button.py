import PySide6.QtCore as QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

import src.icons as icons
from .base import BaseButton
from bin.storage import Storage
from src.icons import ICONS_PATH
from src.styles.components.widgets.buttons import close_button_qss


class MaximizeButton(BaseButton):
    def __init__(self, parent, window):
        super().__init__(parent=parent, onclick=window.showMaximized)

    def make(self):
        self.setIcon(QIcon(str(ICONS_PATH.joinpath(icons.maximize_button_icon))))
        self.setStyleSheet(close_button_qss)
        width, height = self.size().width(), self.size().height()
        width, height = (int(dimension * 0.3) for dimension in (width, height))
        self.setIconSize(QSize(width, height))
