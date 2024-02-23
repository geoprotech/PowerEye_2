from bin.gui.widgets.labels import BaseLabel
from src.styles.components.widgets.pop_up import LABEL_POP_UP_STYLESHEET


class PopUpLabel(BaseLabel):
    def make(self):
        self.setStyleSheet(LABEL_POP_UP_STYLESHEET)
