from PySide6.QtGui import QPixmap

from .base import BaseLabel
from src.styles.components.widgets.labels import IMAGE_LABEL_STYLESHEET


class BaseImageLabel(BaseLabel):
    """
    Base abstract class for all labels.
    Default stylesheet determined here.


    methods:
        make(): Function to create button. Must be overwritten.
        set_tooltip(): Function to set tooltip
        reset_text(): Function to reset text

    """

    def __init__(self, parent=None, text="", pixmap: QPixmap or None = None):
        self.pixmap = pixmap
        super().__init__(parent, text=text)

    def post_setup(self):
        if self.pixmap:
            self.set_pixmap(self.pixmap)

    def make(self):
        self.setStyleSheet(IMAGE_LABEL_STYLESHEET)
        self.post_setup()

    def set_pixmap(self, pixmap: QPixmap):
        self.pixmap = pixmap  # Replace "path_to_your_image.jpg" with the actual path to your image file
        self.pixmap = self.pixmap.scaled(200, 200)

        self.setPixmap(self.pixmap)
