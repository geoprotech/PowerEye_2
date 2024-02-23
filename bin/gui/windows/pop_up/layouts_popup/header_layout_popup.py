from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget

from bin.gui.widgets.layouts import HorizontalLayout
from bin.gui.windows.pop_up.labels_popup import LabelPopUp
from src.styles.components.windows import POP_UP_HEADER_STYLESHEET


class HeaderLayoutPopUp(HorizontalLayout):
    def __init__(self, parent: QWidget, title: str) -> None:
        self.title = title
        super().__init__(parent=parent)

    def make(self):
        self._add_title()
        self.setStyleSheet(POP_UP_HEADER_STYLESHEET)
        self.set_content_margins(0, 0, 0, 0)
        self.set_spacing(0)

    def _add_title(self) -> None:
        title_popup = LabelPopUp(self, text=self.title)
        title_popup.setContentsMargins(0, 0, 0, 0)
        self.add_widget(title_popup, alignment=Qt.AlignLeft)
