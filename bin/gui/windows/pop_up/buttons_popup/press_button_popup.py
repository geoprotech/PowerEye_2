from bin.gui.widgets.buttons.base import BaseButton
from src.styles.components.windows.pop_up import PRESS_BUTTON_POP_UP_STYLESHEET


class PressButtonPopUp(BaseButton):
    def make(self):
        self.setStyleSheet(PRESS_BUTTON_POP_UP_STYLESHEET)
