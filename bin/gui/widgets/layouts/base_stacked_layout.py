from PySide6.QtWidgets import QWidget

from ....exceptions.layout_exception import LayoutException
from .base import BaseLayout


class StackedLayout(BaseLayout):
    """
    - Stacked layout:
    - Inheritance order:
        QWidget -> QFrame -> BaseLayout -> HorizontalLayout
    Public methods:
        - add_tab
        - set_content_margins
        - switch tab
        - same as in QFrame
    Public fields:
        - same as in QFrame
    """

    def __init__(self, parent: QWidget):
        self.__number_of_tabs = 0
        self.tabs = {}
        super(StackedLayout, self).__init__(parent=parent, layout_type="Stacked")

    def add_tab(self, widget: QWidget, tab_name: str) -> None:
        """
        add new tab
        @param widget: QWidget
        @param tab_name: string - name of the tab
        @return: None
        """
        if tab_name in self.tabs:
            raise LayoutException(text="Tab with name '{}' already exist.".format(tab_name), level=1)
        self._layout.addWidget(widget)
        self.tabs[tab_name] = self.__number_of_tabs
        self.__number_of_tabs += 1

    def switch_tab(self, tab_name: str) -> None:
        """
        switch to current tab
        @param tab_name: string - name of the tab
        @return:
        """
        self._layout.setCurrentIndex(self.tabs[tab_name])

    def make(self):
        pass
