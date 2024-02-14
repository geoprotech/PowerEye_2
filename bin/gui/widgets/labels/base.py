from PySide6.QtWidgets import QLabel

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

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent=parent, *args, **kwargs)
        self.make()

    def make(self):
        """
        determ default stylesheet
        """
        self.post_setup()
        self.setStyleSheet(str(LABEL_STYLESHEET))
        # self.setFixedWidth(int(LABEL_STYLESHEET['width']))
        # self.setFixedHeight(int(LABEL_STYLESHEET['height']))

        self.show()

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
