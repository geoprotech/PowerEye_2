from PySide6.QtWidgets import QLineEdit

from src.styles.components.widgets.line_edit import LINE_EDIT_STYLESHEET
from src.styles.stylesheet import Stylesheet


class BaseLineEdit(QLineEdit):
    """
    Base abstract class for all line edit widgets.
        Default stylesheet determined here.


    attributes:
        HOVER_ON - style for hover. No hover style changes if it's not implemented.
        HOVER_OFF - style for hover exit. You can use default stylesheet for button here.

        FOCUS_ON - style for focus. No focus style if it's not implemented.
        FOCUS_OFF - style for unfocused stated. You can use HOVER_ON stylesheet here.

        TOOLTIP_TEXT - text for tooltip. No tooltip if not implemented.

    methods:
        make(): Function to create button. Must be overwritten.
        set_tooltip(): Function to set tooltip

    """

    HOVER_ON: Stylesheet
    HOVER_OFF: Stylesheet

    FOCUS_ON: Stylesheet
    FOCUS_OFF: Stylesheet

    TOOLTIP_TEXT: str

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.make()

    def make(self):
        self.show()
        self.setFixedWidth(int(LINE_EDIT_STYLESHEET['width']))
        self.setFixedHeight(int(LINE_EDIT_STYLESHEET['height']))
        self.setStyleSheet(str(LINE_EDIT_STYLESHEET))

    def set_tooltip(self, text: str):
        """
        set tooltip text
        """
        if text:
            self.setToolTip(text)

    def enterEvent(self, event):  # noqa
        if hasattr(self, "HOVER_ON"):
            self.setStyleSheet(str(self.HOVER_ON))
        return super().enterEvent(event)

    def leaveEvent(self, event):  # noqa
        if hasattr(self, "HOVER_OFF"):
            self.setStyleSheet(str(self.HOVER_OFF))
        return super().leaveEvent(event)

    def focusInEvent(self, event):  # noqa
        if hasattr(self, "FOCUS_ON"):
            self.setStyleSheet(str(self.FOCUS_ON))
        return super().focusInEvent(event)

    def focusOutEvent(self, event):  # noqa
        if hasattr(self, "FOCUS_OFF"):
            self.setStyleSheet(str(self.FOCUS_OFF))
        return super().focusOutEvent(event)
