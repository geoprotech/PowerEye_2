import PySide6.QtCore as QtCore
from PySide6.QtGui import QIcon

from .base import BaseButton
from src.icons import ICONS_PATH
from src.styles.components.widgets.buttons import CLOSE_BUTTON_STYLESHEET, CLOSE_BUTTON_STYLESHEET_HOVER


class CloseButton(BaseButton):
    HOVER_ON = CLOSE_BUTTON_STYLESHEET_HOVER
    HOVER_OFF = CLOSE_BUTTON_STYLESHEET

    def make(self):
        self.setIcon(QIcon(str(ICONS_PATH.joinpath("close_button.png"))))
        self.setStyleSheet(str(CLOSE_BUTTON_STYLESHEET))

        self.clicked.connect(QtCore.QCoreApplication.instance().quit)
