from abc import abstractmethod
from typing import Iterable

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QWidget

from bin.exceptions.base_powereye_exception import BasePowereyeException
from bin.gui.decorators import init_protocol
from bin.gui.widgets.layouts import PopUpHeaderLayout


class SizeException(BasePowereyeException):
    def __init__(self, message):
        super().__init__(message)


@init_protocol
class PopUp(QDialog):
    """
    Base class PopUp Window

        Args:
            parent(QWidget): parent
            title(str): Window title in header
            size(tuple(x: int, y: int,  width: int, height: int)): PopUP size options
    """

    def __init__(self, parent: QWidget, title: str, size: Iterable[int]):
        if len(size) != 4:
            raise SizeException("Invalid number of parameters")

        self.title = title
        self.size = size
        super().__init__(parent=parent)

    def post_setup(self) -> None:
        self.move(*self.size[:2])
        self.resize(*self.size[2:])
        self.setWindowFlag(Qt.FramelessWindowHint)

        self._layout_main = QVBoxLayout()
        self._layout_main.setContentsMargins(0, 0, 0, 0)

        self._pop_up_header_layout = PopUpHeaderLayout(parent=self)

        self._layout_main.addWidget(self._pop_up_header_layout)
        self.setLayout(self._layout_main)

    @abstractmethod
    def make(self) -> None:
        """
        Function to create and configure layout. Must be overridden

            Example:
                self._add_widget(Color('red'))
                button = PopUpCloseButton(self.PopUpHeaderLayout, onclick=self.end)
                self._add_control_buttons(button, alignment=Qt.AlignRight)
        """

    def _add_widget(self, widget: QWidget) -> None:
        self._layout_main.addWidget(widget)

    def _add_control_buttons(
        self, button: QPushButton, stretch: int = 0, alignment: Qt.AlignmentFlag or None = None
    ) -> None:
        self._pop_up_header_layout.add_button(button, stretch, alignment)

    def _add_widget_header(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag or None = None) -> None:
        self._pop_up_header_layout.add_widget(widget, stretch, alignment)

    def show(self):
        self.exec()


#
# class PopUp1(PopUp):
#     def make(self):
#         self._add_widget(Color('red'))
#         self._add_widget(Color('blue'))
#         button = PopUpCloseButton(self._pop_up_header_layout, onclick=self.close)
#         self._add_control_buttons(button, alignment=Qt.AlignRight)
#
#
# import sys
#
# from PySide6.QtWidgets import QApplication, QMainWindow
#
# from bin.gui.widgets.buttons.pop_up_close_button import PopUpCloseButton
# from bin.gui.widgets.stub import Color
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Pop-up окно с PySide6")
#
#         # Создаем кнопку
#         button = QPushButton("Открыть Pop-up окно", self)
#         button.clicked.connect(self.sshow_popup)
#         self.setCentralWidget(button)
#
#     def sshow_popup(self):
#         a = PopUp1(self, 'ali', (0, 300, 500))
#
#
# def run():
#     app = QApplication(sys.argv)
#
#     # Создаем главное окно
#     window = MainWindow()
#     window.show()
#
#     # Запускаем основной цикл обработки событий
#     app.exec()
#
#
# run()
