from typing import Callable

from base_pop_up import BasePopUP
from PySide6.QtCore import Qt

# from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QLabel, QPushButton, QWidget

# from bin.gui.widgets.labels import ImageLabel
from bin.gui.widgets.layouts import HorizontalLayout


# from src.icons import ICONS_PATH, close_button_icon, error_icon


class YesNoPopUP(BasePopUP):
    def __init__(self, parent: QWidget, title: str, message_text: str, on_clik: Callable, *args, **kwargs) -> None:
        self.message_text = message_text
        self.on_clik = on_clik
        super().__init__(parent, title, *args, **kwargs)

    def make(self):
        self._add_title()

        _label = QLabel(text=self.message_text)
        _label.setContentsMargins(20, 20, 20, 20)

        _button_layout = HorizontalLayout(self)

        _accept_button = QPushButton("Accept", self)
        _reject_button = QPushButton("Reject")
        _reject_button.clicked.connect(self.close)
        _accept_button.clicked.connect(self._on_clik)
        _button_layout.add_widget(_reject_button)
        _button_layout.add_widget(_accept_button)
        _button_layout.setContentsMargins(20, 20, 0, 0)

        self.add_widget(_label, alignment=Qt.AlignCenter)
        self.add_widget(_button_layout, alignment=Qt.AlignCenter)

        self._layout_main.setContentsMargins(0, 0, 0, 20)

    def _on_clik(self):
        self.on_clik()
        self.close()
