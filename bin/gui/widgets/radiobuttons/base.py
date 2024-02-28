from PySide6.QtWidgets import QRadioButton, QWidget

from bin.gui.decorators import init_protocol
from src.styles.components.widgets.radiobutton import DEFAULT_RADIOBUTTON_STYLESHEET


class BaseRadioButton(QRadioButton):
    """
    Base abstract class for all radio button widgets.
        Default stylesheet determined here.

    methods:
        make(): Function to create radio button. Must be overwritten.
        set_tooltip(): Function to set tooltip

    """

    @init_protocol
    def __init__(self, parent: QWidget or None, text: str):
        super().__init__(parent=parent, text=text)

    def make(self):
        """
        will be overriden
        """

    def pre_setup(self):
        self.setStyleSheet(DEFAULT_RADIOBUTTON_STYLESHEET)

    def set_tooltip(self, text: str):
        """
        set tooltip text
        """
        if text:
            self.setToolTip(text)
