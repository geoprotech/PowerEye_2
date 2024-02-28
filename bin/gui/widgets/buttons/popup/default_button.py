from bin.gui.widgets.buttons.base import BaseButton
from src.styles.components.widgets.buttons.popup import DEFAULT_POP_UP_BUTTON_STYLESHEET


class PopUpDefaultButton(BaseButton):
    def make(self):
        self.setStyleSheet(DEFAULT_POP_UP_BUTTON_STYLESHEET)

    def on_emit(self):
        """

        @return:
        """
