from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from bin.gui.widgets.labels.popup import PopUpLabel
from bin.gui.widgets.layouts import HorizontalLayout
from src.styles.components.widgets.layouts.popup import POP_UP_HEADER_STYLESHEET


class PopUpHeaderLayout(HorizontalLayout):
    def __init__(self, parent: QWidget, title: str or None) -> None:
        self.title = title
        super().__init__(parent=parent)

    def make(self):
        self._set_title()
        self.setObjectName("popup_header")
        self.setStyleSheet(POP_UP_HEADER_STYLESHEET)
        self.set_content_margins(0, 0, 0, 0)
        self.set_spacing(0)

    def _set_title(self) -> None:
        if self.title is None:
            self.title = ''
        title_label = PopUpLabel(self, text=self.title)
        title_label.setContentsMargins(0, 0, 0, 0)
        self.add_widget(title_label, alignment=Qt.AlignLeft)
