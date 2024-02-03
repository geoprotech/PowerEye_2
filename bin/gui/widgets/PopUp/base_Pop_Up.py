from abc import abstractmethod
from PySide6.QtWidgets import QDialog, QLabel, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt
from bin.gui.widgets.layouts import MainWorkspaceLayout, VerticalLayout, HeaderLayout
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLabel, QHBoxLayout
import sys


class PopUp(QDialog):
    def __init__(self,
                 parent: QWidget,
                 title: str,
                 size: tuple):
        super().__init__(parent=parent)
        self.set_up(title, size)
        self.show_popup()
        self.make()

    def make(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        layout = VerticalLayout(parent=self)
        layout.add_widget(HeaderLayout(parent=self))

    def set_up(self, title: str, size: tuple):
        self.setWindowFlag(Qt.FramelessWindowHint)

    def popup_control_buttons(self, *args, **kwargs):
        pass

    def show_popup(self):
        self.exec()

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
        tt = PopUp(self, 'Test', (0, 0, 200, 200))


def run():
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = MainWindow()
    window.show()

    # Запускаем основной цикл обработки событий
    app.exec()


run()
