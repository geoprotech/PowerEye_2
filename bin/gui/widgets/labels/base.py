from abc import abstractmethod

from PySide6.QtWidgets import QLabel

from bin.gui.decorators import init_protocol
from src.styles.components.widgets.labels import DEFAULT_LABEL_STYLESHEET


class BaseLabel(QLabel):
    """
    Base abstract class for all labels.
    Default stylesheet determined here.


    methods:
        make(): Function to create label. Must be overwritten.
        set_tooltip(): Function to set tooltip
    """

    @init_protocol
    def __init__(self, parent, text: str or None = None, *args, **kwargs):
        super().__init__(parent=parent, text=text, *args, **kwargs)

    @abstractmethod
    def make(self):
        """
        determ default stylesheet
        """

    def pre_setup(self):
        """
        @return:
        """
        self.setStyleSheet(str(DEFAULT_LABEL_STYLESHEET))
