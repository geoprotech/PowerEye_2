from PySide6 import QtCore
from PySide6.QtGui import QPixmap

from bin.gui.widgets.labels import HeaderLabel, ImageLabel
from bin.gui.widgets.layouts import HorizontalLayout
from src.icons import skyrus_logo
from src.styles.components.widgets import HEADER_LOGO_LAYOUT_STYLESHEET


class HeaderLogoLayout(HorizontalLayout):
    def make(self):
        """
        -----------------------
        | logo_img | logo_text |
        -----------------------
        """
        self.setObjectName("header_logo_layout")
        self.setStyleSheet(HEADER_LOGO_LAYOUT_STYLESHEET)
        self.set_content_margins(10, 0, 0, 0)
        self.set_spacing(0)

        self.add_widget(  # logo_img
            ImageLabel(parent=self, pixmap=QPixmap(skyrus_logo), size=[40, 40]), alignment=QtCore.Qt.AlignLeft  # noqa
        )
        self.add_widget(HeaderLabel(parent=self, text="PowerEye"), alignment=QtCore.Qt.AlignLeft)  # logo_text  # noqa
