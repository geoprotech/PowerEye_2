import PySide6.QtCore as QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QLabel, QMainWindow

import bin.gui.widgets.buttons as buttons
import bin.gui.widgets.layouts as layouts
from src.icons import ICONS_PATH
from src.styles.components.windows import MAIN_WINDOW_HEADER_STYLESHEET, MAIN_WINDOW_STYLESHEET


class MainWindow(QMainWindow):
    """
    Configure main window of app.
    """

    def __init__(self) -> None:
        super(MainWindow, self).__init__()

    def make(self):
        self.setGeometry(*MAIN_WINDOW_STYLESHEET.geometry())
        self.setStyleSheet(str(MAIN_WINDOW_STYLESHEET))
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
        main_layout = layouts.MainLayout(self)
        # header_layout = layouts.HeaderLayout(self)

        self.setCentralWidget(main_layout)


