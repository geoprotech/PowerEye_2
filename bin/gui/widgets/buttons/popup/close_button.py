from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon

import src.icons as icons
from bin.gui.widgets.buttons.base import BaseButton
from src.styles.components.widgets.buttons.popup import POP_UP_CONTROL_BUTTON_STYLESHEET


class PopUpCloseButton(BaseButton):
    def __init__(self, parent, window):
        self.parent = parent
        super().__init__(parent=self.parent, on_click=window.close)

    def make(self) -> None:
        self.setIcon(QIcon(str(icons.close_button_icon)))
        width, height = self.size().width(), self.size().height()
        width, height = (int(dimension * 0.3) for dimension in (width, height))
        self.setIconSize(QSize(width, height))
        self.setStyleSheet(POP_UP_CONTROL_BUTTON_STYLESHEET)
