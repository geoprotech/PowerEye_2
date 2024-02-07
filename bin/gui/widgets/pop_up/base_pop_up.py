import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget

import bin.gui.widgets.buttons as buttons
from bin.gui.widgets.layouts import HeaderLayout, VerticalLayout
from bin.gui.widgets.layouts.base_horizontal_layout import HorizontalLayout
from bin.gui.widgets.stub import Color
from src.icons import ICONS_PATH
from src.styles.components.widgets.buttons import CLOSE_BUTTON_STYLESHEET, CLOSE_BUTTON_STYLESHEET_HOVER
from src.styles.components.widgets.pop_up.object import POP_UP_HEADER_STYLESHEET


class CloseButtonPopUp(buttons.BaseButton):
    HOVER_ON = CLOSE_BUTTON_STYLESHEET_HOVER
    HOVER_OFF = CLOSE_BUTTON_STYLESHEET

    def __init__(self, parent):
        super().__init__(parent=parent, onclick=self.close_pop_up)
        self.parent = parent

    def close_pop_up(self):
        self.clicked.connect(self.parent.parent.close())

    def make(self):
        self.setIcon(QIcon(str(ICONS_PATH.joinpath("close_button.png"))))
        self.setStyleSheet(str(CLOSE_BUTTON_STYLESHEET))


class HeaderLayoutPopUp(HeaderLayout):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.parent = parent

    def make(self):
        # self.setFixedHeight(45)
        self.setStyleSheet(str(POP_UP_HEADER_STYLESHEET))
        self.setContentsMargins(0, 0, 0, 0)
        # lll = Color('red')  # QLabel(self, text='Test')

        # text_layout = HorizontalLayout(self)
        text_layout = QLabel(self, text='Test')

        text_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout = HorizontalLayout(self)
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.add_widget(CloseButtonPopUp(self), alignment=Qt.AlignRight)
        # text_layout.add_widget(lll)
        self.add_widget(text_layout)
        self.add_widget(buttons_layout)


class PopUp(QDialog):
    def __init__(self, parent: QWidget, title: str, size: tuple):
        super().__init__(parent=parent)
        self.title_popup = title
        self.make()
        # self.setMaximumSize(300, 150)  # Устанавливаем фиксированный размер диалога
        self.setMinimumSize(300, 150)
        # self.setMouseTracking(True)
        self.show()

    def make(self):
        self.setWindowFlag(Qt.FramelessWindowHint)

        self._layout_main = QVBoxLayout()
        self._layout_main.setContentsMargins(0, 0, 0, 0)

        self._layout = VerticalLayout(parent=self)
        self._layout.set_content_margins(0, 0, 0, 0)

        self._layout.add_widget(HeaderLayoutPopUp(parent=self), 1)

        self._layout.add_widget(Color('red'), 10)

        self._layout_main.addWidget(self._layout)
        self.setLayout(self._layout_main)

    def popup_control_buttons(self, *args, **kwargs):
        pass

    def show_popup(self):
        self.exec()

    def add_widget(self, widget: QWidget):
        self._layout.add_widget(widget)

    def close(self):
        self.accept()

        #

    # @abstractmethod
    # def add_buttons(self, button:QPushButton, *args, **kwargs):
    #     pass
    #
    # @abstractmethod
    # def add_widget(self, widget: QWidget, *args, **kwargs):
    #     pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pop-up окно с PySide6")

        # Создаем кнопку
        button = QPushButton("Открыть Pop-up окно", self)
        button.clicked.connect(self.sshow_popup)
        self.setCentralWidget(button)

    def sshow_popup(self):
        PopUp(self, 'Test', (0, 0, 200, 200))


def run():
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = MainWindow()
    window.show()

    # Запускаем основной цикл обработки событий
    app.exec()


run()
