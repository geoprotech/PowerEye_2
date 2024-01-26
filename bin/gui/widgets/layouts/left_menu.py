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

        for button in self.buttons.values():
            self.add_widget(button, alignment=QtCore.Qt.AlignTop)

    def init_buttons(self):
        self.buttons = {
            "menu": buttons.LeftMenuBaseIconButton(self, "menu_lines.png", tooltip="Меню"),
            "enter_data": buttons.LeftMenuBaseIconButton(self, "enter_data_button.png", tooltip="Данные"),
            "parameters": buttons.LeftMenuBaseIconButton(self, "parameters_button.png", tooltip="Параметры"),
            "trajectory": buttons.LeftMenuBaseIconButton(self, "trajectory_button.png", tooltip="Траектория"),
            "tnd": buttons.LeftMenuBaseIconButton(self, "tnd_graph_button.png", tooltip="T&D модель"),
            "mask_group": buttons.LeftMenuBaseIconButton(self, "mask_group_button.png", tooltip="хз"),
            "custom_graph": buttons.LeftMenuBaseIconButton(
                self, "custom_graph_button.png", tooltip="Пользовательский график"
            ),
            "stats": buttons.LeftMenuBaseIconButton(self, "stats_button.png", tooltip="Статистика"),
        }
        # подключаем ивенты
        self.buttons["menu"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_menu.emit)
        self.buttons["enter_data"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_enter_data.emit)
        self.buttons["parameters"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_parameters.emit)
        self.buttons["trajectory"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_trajectory.emit)
        self.buttons["tnd"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_tnd.emit)
        self.buttons["mask_group"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_mask_group.emit)
        self.buttons["custom_graph"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_custom_graph.emit)
        self.buttons["stats"].change_onclick_event(MainWorkspaceLayout.instance.switch_to_stats.emit)
