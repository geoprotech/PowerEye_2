from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

from .base import BaseButton
from src.icons import ICONS_PATH
from src.styles.components.widgets.buttons import POP_CLOSE_BUTTON_STYLESHEET, POP_CLOSE_BUTTON_STYLESHEET_HOVER


class CloseButtonPopUp(BaseButton):
    """
    pass
    """

    HOVER_ON = POP_CLOSE_BUTTON_STYLESHEET_HOVER
    HOVER_OFF = POP_CLOSE_BUTTON_STYLESHEET

    def __init__(self, parent, onclick):
        super().__init__(parent=parent, onclick=onclick)
        self.parent = parent

    def make(self) -> None:
        self.setIcon(QIcon(str(ICONS_PATH.joinpath("close_button.png"))))
        self.setStyleSheet(str(POP_CLOSE_BUTTON_STYLESHEET))
        self.setFixedHeight(int(POP_CLOSE_BUTTON_STYLESHEET['height']))
        size = self.size()
        icon_width = int(size.width())
        icon_height = int(size.height())
        self.setIconSize(QSize(icon_width, icon_height))
