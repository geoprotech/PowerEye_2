from base_pop_up import BasePopUP
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QPushButton, QWidget

from bin.gui.widgets.layouts import HorizontalLayout
from bin.gui.windows.pop_up import ImageLabelPopUp, PopUpLabel
from src.icons import warning_icon


# from src.icons import ICONS_PATH, close_button_icon,

# from src.icons import ICONS_PATH, close_button_icon


class AlertPopUP(BasePopUP):
    def __init__(self, parent: QWidget, title: str, alert_text: str, *args, **kwargs) -> None:
        self.alert_text = alert_text
        super().__init__(parent, title, *args, **kwargs)

    def make(self):
        self._add_title()

        error_layout = HorizontalLayout(self)

        label = PopUpLabel(parent=self, text=self.alert_text)

        # icon = QIcon(str(warning_icon))
        # icon = icon.pixmap(50, 50)
        # warning_label = QLabel()
        # warning_label.setPixmap(icon)

        warning_label = ImageLabelPopUp(self, pixmap=QPixmap(warning_icon), size=(40, 40))
        # widget_test = HorizontalLayout(parent=self)
        # widget_test.add_widget(Color('red'))
        # widget_test.setFixedWidth(40)
        # widget_test.setFixedHeight(40)

        error_layout.add_widget(warning_label, alignment=Qt.AlignLeft)
        # error_layout.add_widget(widget_test, alignment=Qt.AlignLeft)
        error_layout.add_widget(label, alignment=Qt.AlignCenter)
        # error_layout.add_widget(Color('red'), alignment=Qt.AlignCenter)
        error_layout.set_content_margins(0, 0, 0, 0)
        error_layout.set_spacing(0)
        button = QPushButton("Ок", self)
        button.clicked.connect(self.close)

        self.add_widget(error_layout, alignment=Qt.AlignCenter)
        self.add_widget(button, alignment=Qt.AlignCenter)
        self.set_content_margins(0, 0, 0, 10)
        self.set_spacing(0)
