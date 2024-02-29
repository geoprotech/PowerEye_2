import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from bin.gui.windows.popup import PopUp, WarningPopUp, YesNoPopUp


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
        YesNoPopUp(
            self,
            None,
            'Долбень, неверное количество столбцов',
            on_click_accept=MainWindow.ttt,
            on_click_reject=MainWindow.ttt,
        )
        WarningPopUp(self, 'Title', 'Долбень, неверное количество столбцов')
        PopUp(
            self,
            'VBox',
            None,
        )


def run():
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = MainWindow()
    window.show()

    # Запускаем основной цикл обработки событий
    app.exec()


run()
