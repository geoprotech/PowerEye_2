from ..stub import Color
from .base_stacked_layout import StackedLayout


class MainWorkspaceLayout(StackedLayout):
    def make(self):
        print("make")
        self.add_tab(Color("green"), tab_name="file_import")
        self.add_tab(Color("brown"), tab_name="stats")
        self.switch_tab("file_import")
