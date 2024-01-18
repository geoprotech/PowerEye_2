from abc import abstractmethod

from PySide6.QtWidgets import QPushButton, QWidget

from src.styles.stylesheet import Stylesheet


class BaseButton(QPushButton):
    """
    Base abstract class for all buttons.

    attributes:
        HOVER_ON - style for hover. No hover style changes if it's not implemented.
        HOVER_OFF - style for hover exit. You can use default stylesheet for button here.

        FOCUS_ON - style for focus. No focus style if it's not implemented.
        FOCUS_OFF - style for unfocused stated. You can use HOVER_ON stylesheet here.

        TOOLTIP_TEXT - text for tooltip. No tooltip if not implemented.

    methods:
        make(): Function to create button. Must be overwritten.

    """

    HOVER_ON: Stylesheet
    HOVER_OFF: Stylesheet

    FOCUS_ON: Stylesheet
    FOCUS_OFF: Stylesheet

    TOOLTIP_TEXT: str

    def __init__(self, parent: QWidget):
        super(BaseButton, self).__init__(parent=parent)
        self.make()
        self.show()

    @abstractmethod
    def make(self):
        pass

    def enterEvent(self, event):  # noqa
        if hasattr(self, "HOVER_ON"):
            self.setStyleSheet(str(self.HOVER_ON))
        return super(BaseButton, self).enterEvent(event)

    def leaveEvent(self, event):  # noqa
        if hasattr(self, "HOVER_OFF"):
            self.setStyleSheet(str(self.HOVER_OFF))
        return super(BaseButton, self).leaveEvent(event)

    def focusInEvent(self, event):  # noqa
        if hasattr(self, "FOCUS_ON"):
            self.setStyleSheet(str(self.FOCUS_ON))
        return super(BaseButton, self).focusInEvent(event)

    def focusOutEvent(self, event):  # noqa
        if hasattr(self, "FOCUS_OFF"):
            self.setStyleSheet(str(self.FOCUS_OFF))
        return super(BaseButton, self).focusOutEvent(event)
