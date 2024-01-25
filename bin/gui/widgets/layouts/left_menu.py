import PySide6.QtCore as QtCore
from PySide6.QtWidgets import QPushButton

import bin.gui.widgets.buttons as buttons
from .base_vertical_layout import VerticalLayout
from .main_workspace import MainWorkspaceLayout
from src.styles.components.widgets import LEFT_MENU_STYLESHEET


class LeftMenu(VerticalLayout):
    def __init__(self, parent):
        self.buttons: dict[QPushButton] = {}
        super().__init__(parent=parent)

    def make(self):
        self.init_buttons()

        self.setStyleSheet(str(LEFT_MENU_STYLESHEET))
        self.setFixedWidth(int(LEFT_MENU_STYLESHEET['width']))

        # self.buttons["stats"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_stats.emit)
        for button in self.buttons.values():
            self.add_widget(button, alignment=QtCore.Qt.AlignTop)

    def init_buttons(self):
        self.buttons = {
            "menu": buttons.MenuButton(self),
            "enter_data": buttons.EnterDataButton(self),
            "parameters": buttons.ParametersButton(self),
            "trajectory": buttons.TrajectoryButton(self),
            "tnd": buttons.TndButton(self),
            "mask_group": buttons.MaskGroupButton(self),
            "custom_graph": buttons.CustomGraphButton(self),
            "stats": buttons.StatsButton(self),
        }
        self.buttons["menu"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_menu.emit)
        self.buttons["enter_data"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_enter_data.emit)
        self.buttons["parameters"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_parameters.emit)
        self.buttons["trajectory"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_trajectory.emit)
        self.buttons["tnd"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_tnd.emit)
        self.buttons["mask_group"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_mask_group.emit)
        self.buttons["custom_graph"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_custom_graph.emit)
        self.buttons["stats"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_stats.emit)
