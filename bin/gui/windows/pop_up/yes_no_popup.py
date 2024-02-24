from typing import Callable, Literal

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from .base_popup import BasePopUp
from bin.gui.widgets.layouts import HorizontalLayout
from bin.gui.windows.pop_up.buttons_popup import PressButtonPopUp
from bin.gui.windows.pop_up.labels_popup import LabelPopUp


class YesNoPopUp(BasePopUp):
    def __init__(
        self,
        parent: QWidget,
        layout_type_body: Literal[
            "HBox",
            "VBox",
        ],
        title: str,
        message_text: str,
        on_click: Callable,
        *args,
        **kwargs
    ) -> None:
        self.message_text = message_text
        self.on_click = self._on_click(on_click)
        super().__init__(parent=parent, layout_type_body=layout_type_body, title=title, *args, **kwargs)

    def make(self):
        text_label = LabelPopUp(parent=self, text=self.message_text)

        button_layout = HorizontalLayout(self)

        accept_button = PressButtonPopUp(parent=self, on_click=self.on_click, text="Accept")
        reject_button = PressButtonPopUp(parent=self, on_click=self.close, text="Reject")
        button_layout.add_widget(reject_button, alignment=Qt.AlignCenter)
        button_layout.add_widget(accept_button, alignment=Qt.AlignCenter)
        button_layout.set_content_margins(0, 10, 0, 10)

        self.add_widget(text_label, alignment=Qt.AlignCenter)
        self.add_widget(
            button_layout,
        )

    def _on_click(self, func: Callable) -> Callable:
        def wrapper():
            self.close()
            return func()

        return wrapper
