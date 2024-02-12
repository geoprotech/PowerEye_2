from PySide6.QtWidgets import QLabel

from src.styles.components.widgets.labels import LABEL_STYLESHEET
from src.styles.stylesheet import Stylesheet


class BaseLabel(QLabel):
    """
    Base abstract class for all labels.
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
        reset_text(): Function to reset text

    """

    HOVER_ON: Stylesheet
    HOVER_OFF: Stylesheet

    FOCUS_ON: Stylesheet
    FOCUS_OFF: Stylesheet

    TOOLTIP_TEXT: str

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        self.make()

    def make(self):
        """
        determ default stylesheet
        """
        self.setStyleSheet(str(LABEL_STYLESHEET))
        self.setFixedWidth(int(LABEL_STYLESHEET['width']))
        self.setFixedHeight(int(LABEL_STYLESHEET['height']))

        self.show()

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
