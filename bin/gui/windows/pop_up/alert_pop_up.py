from base_pop_up import BasePopUP
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

# from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLabel, QPushButton, QWidget

from bin.gui.widgets.labels import ImageLabel
from bin.gui.widgets.layouts import HorizontalLayout
from src.icons import warning_icon


# from src.icons import ICONS_PATH, close_button_icon,

# from src.icons import ICONS_PATH, close_button_icon


class AlertPopUP(BasePopUP):
    def __init__(self, parent: QWidget, title: str, alert_text: str, *args, **kwargs) -> None:
        self.alert_text = alert_text
        super().__init__(parent, title, *args, **kwargs)

    def make(self):
        self._add_title()

        _error_layout = HorizontalLayout(self)

        _label = QLabel(text=self.alert_text)

        # _icon = QIcon(str(error_icon))
        # _icon = _icon.pixmap(200,200)
        # _warning_label = QLabel()
        # _warning_label.setPixmap(_icon)
        _warning_label = ImageLabel(
            self,
            pixmap=QPixmap(warning_icon),
            size=(40, 40),
        )
        # _warning_label.setPixmap(QPixmap(error_icon))

        _error_layout.add_widget(_warning_label, alignment=Qt.AlignLeft)
        _error_layout.add_widget(_label, alignment=Qt.AlignCenter)

        _button = QPushButton("Ок", self)
        _button.clicked.connect(self.close)

        self.add_widget(_error_layout, alignment=Qt.AlignCenter)
        self.add_widget(_button, alignment=Qt.AlignCenter)
        self._layout_main.setContentsMargins(0, 0, 0, 20)
        self._layout_main.setSpacing(0)
