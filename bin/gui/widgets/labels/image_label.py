from PySide6.QtGui import QPixmap

from .base import BaseLabel
from src.styles.components.widgets.labels import DEFAULT_IMAGE_LABEL_STYLESHEET


class ImageLabel(BaseLabel):
    """
    Base abstract class for all labels.
    Default stylesheet determined here.


    methods:
        make(): Function to create label. Must be overwritten.
        set_tooltip(): Function to set tooltip
        reset_text(): Function to reset text

    """

    def __init__(self, parent=None, text="", pixmap: QPixmap or None = None, size: (int, int) or None = None):
        self._pixmap = pixmap
        self.size = size
        super().__init__(parent, text=text)

    def pre_setup(self):
        if not self.size:
            self.size = (200, 200)
        if self._pixmap:
            self.set_pixmap(self._pixmap)
        self.setStyleSheet(DEFAULT_IMAGE_LABEL_STYLESHEET)

    def make(self):
        """
        to set up
        @return:
        """

    def set_pixmap(self, pixmap: QPixmap, size: [int, int] or None = None):
        self._pixmap = pixmap  # Replace "path_to_your_image.jpg" with the actual path to your image file
        if size:
            self.size = size
        self._pixmap = self._pixmap.scaled(*self.size)
        self.setPixmap(self._pixmap)
