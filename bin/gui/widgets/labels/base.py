from PySide6.QtWidgets import QLabel

from bin.gui.decorators import init_protocol
from src.styles.components.widgets.labels import LABEL_STYLESHEET


class BaseLabel(QLabel):
    """
    Base abstract class for all labels.
    Default stylesheet determined here.


    methods:
        make(): Function to create button. Must be overwritten.
        set_tooltip(): Function to set tooltip
        reset_text(): Function to reset text

    """

    @init_protocol
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)

    def make(self):
        """
        determ default stylesheet
        """
        self.post_setup()
        self.setStyleSheet(str(LABEL_STYLESHEET))

    def post_setup(self):
        """
        abstract method
        @return:
        """

    def reset_text(self, text: str) -> None:
        """
        reset text in label
        """
        self.setText(text)

    def set_tooltip(self, text: str):
        """
        set tooltip text
        """
        if text:
            self.setToolTip(text)
