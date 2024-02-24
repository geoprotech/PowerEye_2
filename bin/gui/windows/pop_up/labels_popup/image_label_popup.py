from bin.gui.widgets.labels import ImageLabel
from src.styles.components.windows.pop_up import DEFAULT_IMAGE_LABEL_POP_UP_STYLESHEET


class ImageLabelPopUp(ImageLabel):
    def make(self):
        self.setStyleSheet(DEFAULT_IMAGE_LABEL_POP_UP_STYLESHEET)
