import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from bin.gui.windows.popup import PopUp, YesNoPopUp


# from bin.gui.windows.popup import WarningPopUp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pop-up окно с PySide6")
        self.setGeometry(100, 100, 400, 300)

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
            'Долбень, неверное количество столбцов',
            on_click_accept=MainWindow.ttt,
            on_click_reject=MainWindow.ttt,
        )

        # WarningPopUp(self, warning_text='Долбень, неверное количество столбцов')
        PopUp(self, title='Test')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = MainWindow()
    window.show()

    # Запускаем основной цикл обработки событий
    app.exec()
