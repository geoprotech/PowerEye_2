from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget

from .base_popup import BasePopUp
from bin.gui.widgets.buttons.popup import PopUpDefaultButton
from bin.gui.widgets.labels.popup import PopUpImageLabel, PopUpLabel
from bin.gui.widgets.layouts import HorizontalLayout
from src.icons import warning_icon


class WarningPopUp(BasePopUp):
    def __init__(self, parent: QWidget, title: str or None, warning_text: str) -> None:
        self.warning_text = warning_text
        super().__init__(parent=parent, body_layout="VBox", title=title)

    def make(self):
        main_layout = HorizontalLayout(self)

        text_label = PopUpLabel(parent=self, text=self.warning_text)
        label_image = PopUpImageLabel(self, pixmap=QPixmap(warning_icon), size=(40, 40))

        main_layout.add_widget(label_image, alignment=Qt.AlignLeft)
        main_layout.add_widget(text_label, alignment=Qt.AlignCenter)

        main_layout.set_content_margins(0, 0, 0, 0)
        main_layout.set_spacing(0)

        self.add_widget(main_layout, alignment=Qt.AlignCenter)
        self.add_widget(PopUpDefaultButton(self, self.close, text='Ok'), alignment=Qt.AlignCenter)

        self.set_content_margins(0, 0, 0, 10)
        self.set_spacing(0)
