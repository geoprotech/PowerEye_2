from bin.gui.widgets.labels import BaseLabel
from src.styles.components.widgets.labels.popup import DEFAULT_POP_UP_LABEL_STYLESHEET


class PopUpLabel(BaseLabel):
    def make(self):
        self.setStyleSheet(DEFAULT_POP_UP_LABEL_STYLESHEET)
