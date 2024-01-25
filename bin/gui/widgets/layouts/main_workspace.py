import PySide6.QtCore as QtCore

from ..stub import Color
from .base_stacked_layout import StackedLayout


class MainWorkspaceLayout(StackedLayout):
    instance = None

    switch_to_menu = QtCore.Signal()
    switch_to_enter_data = QtCore.Signal()
    switch_to_parameters = QtCore.Signal()
    switch_to_trajectory = QtCore.Signal()
    switch_to_tnd = QtCore.Signal()
    switch_to_mask_group = QtCore.Signal()
    switch_to_custom_graph = QtCore.Signal()
    switch_to_stats = QtCore.Signal()

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(MainWorkspaceLayout, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def make(self):
        self.add_tab(Color("red"), tab_name="menu")
        self.add_tab(Color("orange"), tab_name="enter_data")
        self.add_tab(Color("yellow"), tab_name="parameters")
        self.add_tab(Color("green"), tab_name="trajectory")
        self.add_tab(Color("blue"), tab_name="tnd")
        self.add_tab(Color("purple"), tab_name="mask_group")
        self.add_tab(Color("gray"), tab_name="custom_graph")
        self.add_tab(Color("pink"), tab_name="stats")
        self.switch_tab("menu")
        self.switch_to_menu.connect(self.on_switch_to_menu)
        self.switch_to_enter_data.connect(self.on_switch_to_enter_data)
        self.switch_to_parameters.connect(self.on_switch_to_parameters)
        self.switch_to_trajectory.connect(self.on_switch_to_trajectory)
        self.switch_to_tnd.connect(self.on_switch_to_tnd)
        self.switch_to_mask_group.connect(self.on_switch_to_mask_group)
        self.switch_to_custom_graph.connect(self.on_switch_to_custom_graph)
        self.switch_to_stats.connect(self.on_switch_to_stats)

    def on_switch_to_menu(self):
        self.switch_tab("menu")

    def on_switch_to_enter_data(self):
        self.switch_tab("enter_data")

    def on_switch_to_parameters(self):
        self.switch_tab("parameters")

    def on_switch_to_trajectory(self):
        self.switch_tab("trajectory")

    def on_switch_to_tnd(self):
        self.switch_tab("tnd")

    def on_switch_to_mask_group(self):
        self.switch_tab("mask_group")

    def on_switch_to_custom_graph(self):
        self.switch_tab("custom_graph")

    def on_switch_to_stats(self):
        self.switch_tab("stats")
