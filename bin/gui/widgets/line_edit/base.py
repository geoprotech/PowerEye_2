from PySide6.QtWidgets import QLineEdit

from src.styles.components.widgets.line_edit import LINE_EDIT_STYLESHEET


class BaseLineEdit(QLineEdit):
    """
    Base abstract class for all line edit widgets.
        Default stylesheet determined here.

    methods:
        make(): Function to create button. Must be overwritten.
        set_tooltip(): Function to set tooltip

    """

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.make()

    def make(self):
        self.show()
        # self.setAlignment(QtCore.Qt.AlignLeft)
        self.setStyleSheet(LINE_EDIT_STYLESHEET)

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
