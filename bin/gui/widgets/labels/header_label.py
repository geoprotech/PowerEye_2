from bin.gui.widgets.labels import BaseLabel
from src.styles.components.widgets import HEADER_LABEL_STYLESHEET


class HeaderLabel(BaseLabel):
    def make(self):
        self.setStyleSheet(HEADER_LABEL_STYLESHEET)
