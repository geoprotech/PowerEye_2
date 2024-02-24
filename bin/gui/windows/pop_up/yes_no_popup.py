from typing import Callable

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from .base_popup import BasePopUp
from bin.gui.widgets.buttons.popup import PopUpDefaultButton
from bin.gui.widgets.labels.popup import PopUpLabel
from bin.gui.widgets.layouts import HorizontalLayout


class YesNoPopUp(BasePopUp):
    def __init__(
        self,
        parent: QWidget,
        title: str or None,
        message_text: str,
        on_click_accept: Callable or None,
        on_click_reject: Callable or None,
    ) -> None:
        self.message_text = message_text
        self.on_click_accept = self._deco_on_click(on_click_accept)
        self.on_click_reject = self._deco_on_click(on_click_reject)

        super().__init__(
            parent=parent,
            body_layout_type="VBox",
            title=title,
        )

    def make(self):
        text_label = PopUpLabel(parent=self, text=self.message_text)

        button_layout = HorizontalLayout(self)

        button_layout.add_widget(
            PopUpDefaultButton(parent=self, on_click=self.on_click_accept, text="Accept"), alignment=Qt.AlignCenter
        )
        button_layout.add_widget(
            PopUpDefaultButton(parent=self, on_click=self.on_click_reject, text="Reject"), alignment=Qt.AlignCenter
        )
        button_layout.set_content_margins(0, 10, 0, 10)

        self.add_widget(text_label, alignment=Qt.AlignCenter)
        self.add_widget(button_layout)

    def _deco_on_click(self, func: Callable or None) -> Callable:
        if func is None:
            return self.close

        else:

            def wrapper(*args, **kwargs):
                self.close()
                return func(*args, **kwargs)

            return wrapper
