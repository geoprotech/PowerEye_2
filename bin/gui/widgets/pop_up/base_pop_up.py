from abc import abstractmethod

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QWidget

from bin.gui.decorators import init_protocol
from bin.gui.widgets.layouts import HeaderLayoutPopUp, VerticalLayout


@init_protocol
class PopUp(QDialog):
    """ """

    def __init__(self, parent: QWidget, title: str, size: tuple):
        self.title_popup = title
        self.size = size
        super().__init__(parent=parent)

    def make(self) -> None:
        self.setMinimumSize(*self.size[2:])
        self.setWindowFlag(Qt.FramelessWindowHint)

        self._layout_main = QVBoxLayout()
        self._layout_main.setContentsMargins(0, 0, 0, 0)

        self._layout = VerticalLayout(parent=self)
        self._layout.set_content_margins(0, 0, 0, 0)

        self.headerlayoutPopUp = HeaderLayoutPopUp(parent=self)
        self._layout.add_widget(self.headerlayoutPopUp)

        self._layout_main.addWidget(self._layout)
        self.setLayout(self._layout_main)

    def add_widget(self, widget: QWidget) -> None:
        self._layout.add_widget(widget)

    def add_contol_buttons(
        self, button: QPushButton, stretch: int = 0, alignment: Qt.AlignmentFlag or None = None
    ) -> None:
        self.headerlayoutPopUp.add_button(button, stretch, alignment)

    @abstractmethod
    def post_setup(self):
        """ """

    def end(self) -> None:
        self.accept()


"""
Test
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from bin.gui.widgets.buttons.pop_up_close_button import CloseButtonPopUp
from bin.gui.widgets.stub import Color
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pop-up окно с PySide6")

        # Создаем кнопку
        button = QPushButton("Открыть Pop-up окно", self)
        button.clicked.connect(self.sshow_popup)
        self.setCentralWidget(button)

    def sshow_popup(self):
        a = PopUp(self, 'ali', (0, 0, 300, 500))
        a.add_widget(Color('red'))
        t = CloseButtonPopUp(a.headerlayoutPopUp, onclick=a.end)
        a.add_contol_buttons(t)


def run():
    app = QApplication(sys.argv)

    # Создаем главное окно
    window = MainWindow()
    window.show()

    # Запускаем основной цикл обработки событий
    app.exec()


run()
"""
