import sys

from alert_pop_up import AlertPopUP
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# from pop_up import PopUp


class PopUp1(AlertPopUP):
    def make(self):
        super().make()
        self.set_size(500, 500, 400, 100)


# from bin.gui.widgets.buttons.pop_up_close_button import PopUpCloseButton
# from bin.gui.widgets.stub import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pop-up окно с PySide6")

        # Создаем кнопку
        button = QPushButton("Открыть Pop-up окно", self)
        button.clicked.connect(self.sshow_popup)
        self.setCentralWidget(button)

    @staticmethod
    def ttt():
        print('aaaaaaaaaaaaaaaa')

    def sshow_popup(self):
        # PopUp1(self, 'Error', 'Долбень, неверное количество столбцов', on_clik=MainWindow.ttt)
        PopUp1(self, 'Error', 'Долбень, неверное количество столбцов')


def run():
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = MainWindow()
    window.show()

    # Запускаем основной цикл обработки событий
    app.exec()


run()
