import PySide6.QtCore as QtCore
from PySide6.QtGui import QColor, QIcon, QPalette
from PySide6.QtWidgets import QMainWindow, QWidget

import bin.gui.widgets.layouts as layouts
from src.icons import ICONS_PATH
from src.styles.components.windows import MAIN_WINDOW_STYLESHEET


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

    def change_color(self, color):
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


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
        # widget = QFrame()
        # layout = QVBoxLayout()
        # layout.setContentsMargins(0, 0, 0, 0)
        # widget.setLayout(layout)
        # self.setCentralWidget(widget)
        #
        # self.widget_red = Color("red")
        # self.widget_red.setGeometry(2, 2, 2, 2)
        # self.widget_red.setFixedHeight(300)
        # layout.addWidget(self.widget_red, 3)
        # layout.addWidget(Color("green"), 1)
        # layout.addWidget(Color("blue"), 2)
        # self.widget_red.change_color("black")
