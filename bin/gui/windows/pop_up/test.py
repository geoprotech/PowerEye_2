import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from bin.gui.windows.pop_up import AlertPopUp, PopUp, YesNoPopUp


# from popup import PopUp


# class PopUp1(PopUp):
# def make(self):
#     super().make()
# self.set_geometry(500, 500, 400, 100)


# from bin.gui.widgets.buttons.control_buttons_pop_up import CloseButtonPopUp
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
        YesNoPopUp(self, 'VBox', 'Error', 'Долбень, неверное количество столбцов', on_click=MainWindow.ttt)
        AlertPopUp(self, 'VBox', 'Error', 'Долбень, неверное количество столбцов')
        PopUp(
            self,
            'VBox',
            'Error',
        )


def run():
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = MainWindow()
    window.show()

    # Запускаем основной цикл обработки событий
    app.exec()


run()
