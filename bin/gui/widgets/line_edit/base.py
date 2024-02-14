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

    def make(self):
        # self.setAlignment(QtCore.Qt.AlignLeft)
        self.setStyleSheet(LINE_EDIT_STYLESHEET)

    def post_setup(self):
        """
        post setup config
        @return:
        """

    def set_tooltip(self, text: str):
        """
        set tooltip text
        """
        if text:
            self.setToolTip(text)
