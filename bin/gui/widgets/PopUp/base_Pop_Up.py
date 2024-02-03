from abc import abstractmethod
from PySide6.QtWidgets import QDialog, QLabel, QWidget, QPushButton, QVBoxLayout
from PySide6.QtCore import Qt

import bin.gui.widgets.buttons as buttons


class PopUp(QDialog):
    def __init__(self,
                 parent: QWidget,
                 title: str,
                 size: tuple):
        super().__init__(parent=parent)
        self.set_up(title, size)
        self.show_popup()

    def post_setup(self):
        layoutV = QVBoxLayout()
        layoutV.addWidget(VerticalLayout(parent = self))
        self.setLayout(layoutV)

    def set_up(self, title: str, size: tuple):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(*size)

    def popup_control_buttons(self, *args, **kwargs):
        pass


    def show_popup(self):
        self.exec()

    @abstractmethod
    def make(self):
        pass

    @abstractmethod
    def add_buttons(self, button:QPushButton, *args, **kwargs):
        pass

    @abstractmethod
    def add_widget(self, widget: QWidget, *args, **kwargs):
        pass
