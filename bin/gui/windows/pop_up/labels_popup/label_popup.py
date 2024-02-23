from bin.gui.widgets.labels import BaseLabel
from src.styles.components.windows.pop_up import DEFAULT_LABEL_POP_UP_STYLESHEET


class LabelPopUp(BaseLabel):
    def make(self):
        self.setStyleSheet(DEFAULT_LABEL_POP_UP_STYLESHEET)
