from bin.gui.widgets.labels import ImageLabel
from src.styles.components.widgets.labels.popup import DEFAULT_POP_UP_IMAGE_LABEL_STYLESHEET


class PopUpImageLabel(ImageLabel):
    def make(self):
        self.setStyleSheet(DEFAULT_POP_UP_IMAGE_LABEL_STYLESHEET)
