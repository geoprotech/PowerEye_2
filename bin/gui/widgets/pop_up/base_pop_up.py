import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QVBoxLayout, QWidget

from bin.gui.widgets.layouts import HeaderLayout, VerticalLayout
from bin.gui.widgets.stub import Color


class PopUp(QDialog):
    def __init__(self, parent: QWidget, title: str, size: tuple):
        super().__init__(parent=parent)
        self._layout_main = QVBoxLayout()
        self._layout_main.setContentsMargins(0, 0, 0, 0)
        self._layout = VerticalLayout(parent=self)
        self._layout.set_content_margins(0, 0, 0, 0)
        self._layout.add_widget(HeaderLayout(parent=self))
        self._layout.add_widget(Color('red'))
        self._layout_main.addWidget(self._layout)

        self.setLayout(self._layout_main)
        # self.add_widget(Color("red"))

        self.make()
        self.show()
        # self.show_popup()

    def make(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedWidth(200)
        self.setFixedHeight(200)

    def set_up(self, title: str, size: tuple):
        # self.setWindowFlag(Qt.FramelessWindowHint)
        pass

    def popup_control_buttons(self, *args, **kwargs):
        pass

    def show_popup(self):
        self.exec()

    def add_widget(self, widget: QWidget):
        self._layout.add_widget(widget)

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
