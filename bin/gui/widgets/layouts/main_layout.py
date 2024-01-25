from ..stub import Color
from .base_horizontal_layout import HorizontalLayout
from .base_vertical_layout import VerticalLayout
from .header_layout import HeaderLayout
from .main_workspace import MainWorkspaceLayout


class MainLayout(VerticalLayout):
    """
    Main app layout with header, left panel and main workspace
    """

    def make(self):
        self.set_content_margins(0, 0, 0, 0)

        main_window = HorizontalLayout(parent=self)

        main_window.set_content_margins(0, 0, 0, 0)
        main_window.add_widget(Color('red'), stretch=1)

        main_layout = MainWorkspaceLayout(parent=self)
        main_window.add_widget(main_layout, stretch=10)

        self.add_widget(HeaderLayout(parent=self))
        self.add_widget(main_window)
