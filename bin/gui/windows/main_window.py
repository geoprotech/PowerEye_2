import PySide6.QtCore as QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QLabel, QMainWindow

import bin.gui.widgets.buttons as buttons
from src.icons import ICONS_PATH
from src.styles import BASE_STYLESHEET, MAIN_WINDOW_HEADER_STYLESHEET


class MainWindow(QMainWindow):
    """
    Configure main window of app.
    """

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.header_layout = QHBoxLayout()

    def create_window(self):
        self.setGeometry(*BASE_STYLESHEET.geometry())
        self.setStyleSheet(repr(BASE_STYLESHEET))
        self.setWindowTitle("PowerEye 2.0")
        self.setWindowIcon(QIcon(str(ICONS_PATH.joinpath("skyrus_logo.png"))))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self._setup_header()

        self.show()

    def _setup_header(self) -> None:
        """
        Configure header of main window.
        :return: None
        """
        # Configure header background
        header_background = QLabel()
        header_background.setStyleSheet(repr(MAIN_WINDOW_HEADER_STYLESHEET))
        header_background.setFixedHeight(int(MAIN_WINDOW_HEADER_STYLESHEET["height"]))
        header_background.setLayout(self.header_layout)
        self.setCentralWidget(header_background)

        # Configure close_button
        close_btn = buttons.CloseButton(header_background)
        self.header_layout.addWidget(close_btn, alignment=QtCore.Qt.AlignRight)
