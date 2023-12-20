import PySide6.QtCore as QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QLabel, QMainWindow

import Bin.Gui.Widgets.Buttons as Buttons
from Src.Icons import ICONS_PATH
from Src.Styles.stylesheet import (
    BASE_STYLESHEET,
    MAIN_WINDOW_HEADER_STYLESHEET,
)


class MainWindow(QMainWindow):
    """
    Configure main window of app.
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(*BASE_STYLESHEET.geometry())
        self.setStyleSheet(repr(BASE_STYLESHEET))
        self.setWindowTitle("PowerEye 2.0")
        self.setWindowIcon(QIcon(str(ICONS_PATH.joinpath("skyrus_logo.png"))))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.box_layout = QHBoxLayout()
        self.setLayout(self.box_layout)

        self.header = QLabel(self)
        self._setup_header()
        self.box_layout.addWidget(self.header)

        self.setCentralWidget(self.header)

        self.show()

    def _setup_header(self) -> None:
        """
        Configure header of main window.
        :return: None
        """
        self.header.setStyleSheet(repr(MAIN_WINDOW_HEADER_STYLESHEET))
        self.header.setText("PowerEye")
        self.header.setFixedHeight(
            int(MAIN_WINDOW_HEADER_STYLESHEET["height"])
        )

        btn = Buttons.CloseButton(self)
        self.box_layout.addWidget(btn)
