from .base_horizontal_layout import HorizontalLayout
from .base_vertical_layout import VerticalLayout
from .header_layout import HeaderLayout
from .left_menu import LeftMenu
from .left_menu_stub import LeftMenuStub
from .main_workspace import MainWorkspaceLayout


class MainLayout(VerticalLayout):
    """
    Main app layout with header, left panel and main workspace
    """

    def make(self):
        """
        brief:

        1. self contain:
                -------------------------------------------
                |            HeaderLayout                 |
                -------------------------------------------
                |            main_window                  |
                -------------------------------------------


        2. main window contain:
                -----------------------------------------------
                |  LeftMenu  |          main_layout          |
                -----------------------------------------------

        @return:
        """
        self.set_content_margins(0, 0, 0, 0)
        self.set_spacing(0)

        # main window creation
        main_window = HorizontalLayout(parent=self)
        main_window.set_content_margins(0, 0, 0, 0)
        main_window.set_spacing(0)

        # under header
        main_layout = MainWorkspaceLayout(parent=self)
        main_layout.set_content_margins(0, 0, 0, 0)
        main_layout.set_spacing(0)

        LeftMenu(parent=self).show()  # not in any layout

        # add widgets to main layout
        main_window.add_widget(LeftMenuStub(parent=self))  # just void background
        main_window.add_widget(main_layout)

        # add header and main layout
        self.add_widget(HeaderLayout(parent=self))
        self.add_widget(main_window)
