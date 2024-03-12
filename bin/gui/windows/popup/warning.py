from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from .base import BasePopUp
from bin.gui.widgets.buttons.popup import PopUpDefaultButton
from bin.gui.widgets.labels.popup import PopUpImageLabel, PopUpLabel
from bin.gui.widgets.layouts import HorizontalLayout
from bin.storage import Storage
from src.icons import warning_icon


class WarningPopUp(BasePopUp):
    def __init__(self, warning_text: str, title: str or None = None) -> None:
        self.warning_text = warning_text
        parent = Storage().get("main_window")
        super().__init__(parent=parent, body_layout="VBox", title=title)

    def make(self):
        self.set_geometry(400, 200)

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

    def on_emit(self):
        """

        @return:
        """
