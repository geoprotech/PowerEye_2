from base_pop_up import BasePopUP
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLabel, QPushButton, QWidget

# from bin.gui.widgets.labels import ImageLabel
from bin.gui.widgets.layouts import HorizontalLayout
from src.icons import warning_icon


# from PySide6.QtGui import QPixmap


# from src.icons import ICONS_PATH, close_button_icon,

# from src.icons import ICONS_PATH, close_button_icon


class AlertPopUP(BasePopUP):
    def __init__(self, parent: QWidget, title: str, alert_text: str, *args, **kwargs) -> None:
        self.alert_text = alert_text
        super().__init__(parent, title, *args, **kwargs)

    def make(self):
        self._add_title()

        error_layout = HorizontalLayout(self)

        label = QLabel(text=self.alert_text)

        icon = QIcon(str(warning_icon))
        icon = icon.pixmap(50, 50)
        warning_label = QLabel()
        warning_label.setPixmap(icon)

        # warning_label = ImageLabel(
        #     self,
        #     pixmap=QPixmap(warning_icon),
        #     size=(40, 40)
        # )

        error_layout.add_widget(warning_label, alignment=Qt.AlignLeft)
        error_layout.add_widget(label, alignment=Qt.AlignCenter)
        error_layout.set_content_margins(0, 10, 10, 10)
        button = QPushButton("Ок", self)
        button.clicked.connect(self.close)

        self.add_widget(error_layout, alignment=Qt.AlignCenter)
        self.add_widget(button, alignment=Qt.AlignCenter)
        self.set_content_margins(0, 0, 0, 10)
        self.set_spacing(0)
