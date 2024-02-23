from typing import Literal

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from .base_popup import BasePopUp
from bin.gui.widgets.layouts import HorizontalLayout
from bin.gui.windows.pop_up.buttons_popup import PressButtonPopUp
from bin.gui.windows.pop_up.labels_popup import ImageLabelPopUp, LabelPopUp
from src.icons import warning_icon


class AlertPopUp(BasePopUp):
    def __init__(
        self, parent: QWidget, layout_type_body: Literal["HBox", "VBox"], title: str, alert_text: str, **kwargs
    ) -> None:
        self.alert_text = alert_text
        super().__init__(parent=parent, layout_type_body=layout_type_body, title=title, **kwargs)

    def make(self):
        warning_layout = HorizontalLayout(self)

        warning_text_label = LabelPopUp(parent=self, text=self.alert_text)
        warning_image_label = ImageLabelPopUp(self, pixmap=QPixmap(warning_icon), size=(40, 40))

        warning_layout.add_widget(warning_image_label, alignment=Qt.AlignLeft)
        warning_layout.add_widget(warning_text_label, alignment=Qt.AlignCenter)

        warning_layout.set_content_margins(0, 0, 0, 0)
        warning_layout.set_spacing(0)

        ok_btn = PressButtonPopUp(self, self.close, text='Ok')

        self.add_widget(warning_layout, alignment=Qt.AlignCenter)
        self.add_widget(ok_btn, alignment=Qt.AlignCenter)

        self.set_content_margins(0, 0, 0, 10)
        self.set_spacing(0)
