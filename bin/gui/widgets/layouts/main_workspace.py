import PySide6.QtCore as QtCore

from ..stub import Color
from .base_stacked_layout import StackedLayout
from .enter_data import EnterData
from .playground import PlaygroundLayout


TAB_NAMES = ["menu", "parameters", "trajectory", "tnd", "mask_group", "custom_graph", "stats"]


class MainWorkspaceLayout(StackedLayout):
    """
    Singleton class: instance contains instance
    """

    instance = None

    # signals to accept events from buttons in ./left_menu.py
    switch_to_menu = QtCore.Signal()
    switch_to_enter_data = QtCore.Signal()
    switch_to_parameters = QtCore.Signal()
    switch_to_trajectory = QtCore.Signal()
    switch_to_tnd = QtCore.Signal()
    switch_to_mask_group = QtCore.Signal()
    switch_to_custom_graph = QtCore.Signal()
    switch_to_stats = QtCore.Signal()

    def __new__(cls, *args, **kwargs):
        """
        to create only one instance of this class
        """
        if not cls.instance:
            cls.instance = super(MainWorkspaceLayout, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def make(self):
        self.__create_tabs()
        self.switch_tab("test")
        self.__connect_tabs_to_signals()

    def __create_tabs(self):
        """
        сейчас забито пустышками, далее будут реальные вкладки
        """
        tab_colors = ["red", "orange", "yellow", "blue", "purple", "gray", "pink"]
        for color, name in zip(tab_colors, TAB_NAMES):
            self.add_tab(Color(color), tab_name=name)
            # self.add_tab(QWidget(), tab_name=name)
        self.add_tab(PlaygroundLayout(parent=self), tab_name="test")
        self.add_tab(EnterData(parent=self), tab_name="enter_data")

    def __connect_tabs_to_signals(self):
        """
        connect tabs to signals
        """
        self.switch_to_menu.connect(lambda: self.switch_tab("menu"))
        self.switch_to_enter_data.connect(lambda: self.switch_tab("enter_data"))
        self.switch_to_parameters.connect(lambda: self.switch_tab("parameters"))
        self.switch_to_trajectory.connect(lambda: self.switch_tab("trajectory"))
        self.switch_to_tnd.connect(lambda: self.switch_tab("tnd"))
        self.switch_to_mask_group.connect(lambda: self.switch_tab("mask_group"))
        self.switch_to_custom_graph.connect(lambda: self.switch_tab("custom_graph"))
        self.switch_to_stats.connect(lambda: self.switch_tab("stats"))
