import PySide6.QtCore as QtCore
from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

import src.icons as icons
from .base import BaseButton
from src.styles.components.widgets.buttons import WINDOW_CONTROL_BUTTON_STYLESHEET


class MinimizeButton(BaseButton):
    def __init__(self, parent, window):
        super().__init__(parent=parent, on_click=window.showMinimized)

    def make(self):
        self.setIcon(QIcon(str(icons.minimize_button_icon)))
        self.setStyleSheet(WINDOW_CONTROL_BUTTON_STYLESHEET)
        width, height = self.size().width(), self.size().height()
        width, height = (int(dimension * 0.1) for dimension in (width, height))
        self.setIconSize(QSize(width, height))

    def on_emit(self):
        """
        not necessary here
        @return:
        """
