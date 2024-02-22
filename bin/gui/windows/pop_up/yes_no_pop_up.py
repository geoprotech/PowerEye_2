from typing import Callable

from base_pop_up import BasePopUP
from PySide6.QtCore import Qt

# from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QLabel, QPushButton, QWidget

from bin.gui.widgets.layouts import HorizontalLayout


class YesNoPopUP(BasePopUP):
    def __init__(self, parent: QWidget, title: str, message_text: str, on_clik: Callable, *args, **kwargs) -> None:
        self.message_text = message_text
        self.on_clik = on_clik
        super().__init__(parent, title, *args, **kwargs)

    def make(self):
        self._add_title()

        text_label = QLabel(text=self.message_text)
        text_label.setContentsMargins(20, 20, 20, 20)

        button_layout = HorizontalLayout(self)

        accept_button = QPushButton(
            self,
            text="Accept",
        )
        reject_button = QPushButton(self, text="Reject")
        reject_button.clicked.connect(self.close)
        accept_button.clicked.connect(self._on_clik)
        button_layout.add_widget(reject_button, alignment=Qt.AlignCenter)
        button_layout.add_widget(accept_button, alignment=Qt.AlignCenter)
        button_layout.setContentsMargins(0, 10, 0, 0)

        self.add_widget(text_label, alignment=Qt.AlignCenter)
        self.add_widget(
            button_layout,
        )

        self.set_content_margins(0, 0, 0, 10)

    def _on_clik(self):
        self.on_clik()
        self.close()
