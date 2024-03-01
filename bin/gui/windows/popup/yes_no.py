from typing import Callable

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from .base import BasePopUp
from bin.gui.widgets.buttons.popup import PopUpDefaultButton
from bin.gui.widgets.labels.popup import PopUpLabel
from bin.gui.widgets.layouts import HorizontalLayout


class YesNoPopUp(BasePopUp):
    def __init__(
        self,
        parent: QWidget,
        message_text: str,
        title: str or None = None,
        on_click_accept: Callable or None = None,
        on_click_reject: Callable or None = None,
    ) -> None:
        self.message_text = message_text
        self.on_click_accept = self._decorator_onclick(on_click_accept)
        self.on_click_reject = self._decorator_onclick(on_click_reject)

        super().__init__(parent=parent, body_layout="VBox", title=title)

    def make(self):
        text_label = PopUpLabel(parent=self, text=self.message_text)

        buttons_layout = HorizontalLayout(self)

        buttons_layout.add_widget(
            PopUpDefaultButton(parent=self, on_click=self.on_click_accept, text="Accept"), alignment=Qt.AlignCenter
        )
        buttons_layout.add_widget(
            PopUpDefaultButton(parent=self, on_click=self.on_click_reject, text="Reject"), alignment=Qt.AlignCenter
        )
        buttons_layout.set_content_margins(0, 10, 0, 10)

        self.add_widget(text_label, alignment=Qt.AlignCenter)
        self.add_widget(buttons_layout)

    def _decorator_onclick(self, func: Callable or None) -> Callable:
        if func is None:
            return self.close

        else:

            def wrapper(*args, **kwargs):
                self.close()
                return func(*args, **kwargs)

            return wrapper
