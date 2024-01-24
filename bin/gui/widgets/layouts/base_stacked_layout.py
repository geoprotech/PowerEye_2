from PySide6.QtWidgets import QWidget

from ....exceptions.layout_exception import LayoutException
from .base import BaseLayout


class StackedLayout(BaseLayout):
    def __init__(self, parent: QWidget):
        super().__init__(self, parent, layout_type="Stacked")
        self.__number_of_tabs = 0
        self.__tabs = {}

    def add_tab(self, widget: QWidget, tab_name: str) -> None:
        if tab_name not in self.__tabs:
            raise LayoutException(text="Tab with name '{}' already exist.".format(tab_name), level=1)
        self._layout.addWidget(widget)
        self.__tabs[tab_name] = self.__number_of_tabs
        self.__number_of_tabs += 1

    def switch_tab(self, tab_name: str) -> None:
        self._layout.setCurrentIndex(self.__tabs[tab_name])

    def make(self):
        pass
