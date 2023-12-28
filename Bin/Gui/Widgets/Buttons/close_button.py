import PySide6.QtCore as QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton, QWidget

from Src.Icons import ICONS_PATH


class CloseButton(QPushButton):
    """
    Custom close button on header.
    """

    def __init__(self, parent: QWidget):
        super(CloseButton, self).__init__(parent=parent)
        self.setIcon(QIcon(str(ICONS_PATH.joinpath("close_button.png"))))
        self.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.show()
