from abc import abstractmethod

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget

from bin.gui.decorators import init_protocol
from bin.gui.widgets.layouts import PopUpHeaderLayout


class BasePopUP(QDialog):
    @init_protocol
    def __init__(self, parent: QWidget, title: str, *args, **kwargs):
        self.title = title
        super().__init__(parent=parent, *args, **kwargs)

    def pre_setup(self) -> None:
        self.setWindowFlag(Qt.FramelessWindowHint)

        # self._layout_main = VerticalLayout()  # noqa
        self._layout_main = QVBoxLayout()  # noqa

        self.set_content_margins(0, 0, 0, 0)
        self.set_spacing(0)

        self._pop_up_header_layout = PopUpHeaderLayout(parent=self)  # noqa

        self.add_widget(self._pop_up_header_layout)

        # self.setLayout(QVBoxLayout())
        self.setLayout(self._layout_main)

    @abstractmethod
    def make(self) -> None:
        """
        Function to create and configure layout. Must be overridden

            Example:
                self.add_widget(Color('red'))
        """

    def add_widget(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag or None = None) -> None:
        """
        adds a widget to the layout
        @param widget: QWidget
        @param stretch: int
        @param alignment: Qt.AlignmentFlag or None
        @return: None
        """

        # default alignment непонятно как определяется в Qt, поэтому сделал так
        if alignment:
            self._layout_main.addWidget(widget, stretch, alignment)
        else:
            self._layout_main.addWidget(widget, stretch)

    def _add_title(self) -> None:
        _title_popup = QLabel(self, text=self.title)
        _title_popup.setContentsMargins(0, 0, 0, 0)
        self._pop_up_header_layout.add_widget(_title_popup, alignment=Qt.AlignLeft)

    def set_content_margins(self, left: int, top: int, right: int, bottom: int) -> None:
        self._layout_main.setContentsMargins(left, top, right, bottom)

    def set_spacing(self, spacing: int) -> None:
        self._layout_main.setSpacing(spacing)

    def set_size(self, x: int, y: int, width: int, height: int):
        self.move(x, y)
        self.resize(width, height)

    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Escape:
    #         event.ignore()

    def show(self) -> None:
        self.exec()


# class PopUp1(AlertPopUP):
#     def make(self):
#         super().make()
#         self.move(500, 500)
#         self.resize(400, 200)
#
#
# import sys
#
# from PySide6.QtWidgets import QApplication, QMainWindow
#
# # from bin.gui.widgets.buttons.pop_up_close_button import PopUpCloseButton
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
#         a = PopUp1(self, 'Error','Долбень, неверное количество столбцов')
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
