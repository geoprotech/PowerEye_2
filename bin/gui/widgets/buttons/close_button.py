import PySide6.QtCore as QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QWidget

from src.icons import ICONS_PATH
from src.styles.components.widgets.buttons.close_button import CLOSE_BUTTON_STYLESHEET, CLOSE_BUTTON_STYLESHEET_HOVER


class CloseButton(QPushButton):
    """
    Custom close button on header.
    """

    def __init__(self, parent: QWidget):
        super(CloseButton, self).__init__(parent=parent)
        self.generate()

    def generate(self):
        self.setIcon(QIcon(str(ICONS_PATH.joinpath("close_button.png"))))
        self.setStyleSheet(repr(CLOSE_BUTTON_STYLESHEET))

        self.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.show()

    def enterEvent(self, event):
        self.setStyleSheet(repr(CLOSE_BUTTON_STYLESHEET_HOVER))
        return super(CloseButton, self).enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet(repr(CLOSE_BUTTON_STYLESHEET))
        return super(CloseButton, self).leaveEvent(event)
