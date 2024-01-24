from PySide6 import QtWidgets

from .base_vertical_layout import VerticalLayout
from .base_horizontal_layout import HorizontalLayout
from .header_layout import HeaderLayout
from src.styles.components.windows import MAIN_WINDOW_HEADER_STYLESHEET
import bin.gui.widgets.buttons as buttons
import PySide6.QtCore as QtCore
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QFrame
from PySide6.QtGui import QPalette, QColor


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

class MainLayout(VerticalLayout):
    def make(self):
        self.setStyleSheet("background-color: #FF0000; ")

        self.set_content_margins(0,0,0,0)
        hor_bg = HorizontalLayout(parent=self)
        hor_bg2 = HorizontalLayout(parent=self)
        hor_bg.setStyleSheet("background-color: #000000; height: 100")
        hor_bg2.setStyleSheet("background-color: #0000FF; ")

        self.add_widget(Color("white"), alignment=QtCore.Qt.AlignTop)
        self.add_widget(Color("green"), alignment=QtCore.Qt.AlignTop)
        self.add_widget(Color("blue"), alignment=QtCore.Qt.AlignTop)
        self.adjustSize()

        print(self._layout.maximumSize())

        # self.add_widget(hor_bg2, 2, alignment=QtCore.Qt.AlignTop)