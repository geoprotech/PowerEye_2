from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon

from .base import BaseButton
from src.icons import ICONS_PATH
from src.styles.components.widgets.buttons import LEFT_MENU_BUTTON_STYLESHEET


class LeftMenuIconButton(BaseButton):
    def __init__(self, parent, icon: str, tooltip: str or None = None, text: str = ""):
        """
        @param parent: QWidget parent
        @param icon_name: name of file from icons folder
        @param tooltip: string of tooltip (optionally)
        """
        self.__icon = icon
        self.text = text
        super().__init__(parent=parent, tooltip=tooltip)

    def make(self):
        self.setText(f"   {self.text}")  # for distance between icon and text
        self.setIcon(QIcon(str(ICONS_PATH.joinpath(self.__icon))))
        self.setStyleSheet(LEFT_MENU_BUTTON_STYLESHEET)
        size = self.size()
        icon_width = 45
        icon_height = size.height()
        self.setIconSize(QSize(icon_width, icon_height))
        self.setContentsMargins(0, 0, 0, 0)

    def on_emit(self):
        """
        not necessary here
        @return:
        """
