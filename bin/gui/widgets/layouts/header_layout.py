from .base_horizontal_layout import HorizontalLayout
from bin.gui.widgets.layouts.header_buttons_layout import HeaderButtonsLayout
from bin.gui.widgets.layouts.header_logo_layout import HeaderLogoLayout
from src.styles.components.widgets.layouts import HEADER_STYLESHEET


class HeaderLayout(HorizontalLayout):
    """
    Header layout for application header
    """

    def make(self):
        """
        ----------------------------------------------------------------
        | Logo      | void        | buttons (minimize, maximize, close) |
        ----------------------------------------------------------------
        """

        self.setObjectName("header")
        self.setStyleSheet(HEADER_STYLESHEET)
        self.set_content_margins(0, 0, 0, 1)
        self.set_spacing(0)

        self.add_widget(HeaderLogoLayout(parent=self))  # logo
        self.add_widget(HorizontalLayout(parent=self))  # void
        self.add_widget(HeaderButtonsLayout(parent=self))  # buttons
