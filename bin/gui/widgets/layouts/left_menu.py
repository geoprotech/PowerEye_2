import PySide6.QtCore as QtCore

import src.icons as icons
import bin.gui.widgets.buttons as buttons
from .base_vertical_layout import VerticalLayout
from .main_workspace import MainWorkspaceLayout
from src.styles.components.widgets import LEFT_MENU_STYLESHEET


BUTTONS_CONFIG = {
    "menu": {"kwargs": {"icon": icons.menu_button_icon, "tooltip": "Меню"}},
    "enter_data": {"kwargs": {"icon": icons.enter_data_button_icon, "tooltip": "Данные"}},
    "parameters": {"kwargs": {"icon": icons.parameters_button_icon, "tooltip": "Параметры"}},
    "trajectory": {"kwargs": {"icon": icons.trajectory_button_icon, "tooltip": "Траектория"}},
    "tnd": {"kwargs": {"icon": icons.tnd_button_icon, "tooltip": "T&D модель"}},
    "mask_group": {"kwargs": {"icon": icons.mask_group_button_icon, "tooltip": "Дифф. подлипания"}},
    "custom_graph": {"kwargs": {"icon": icons.custom_graph_button_icon, "tooltip": "Пользовательский график"}},
    "stats": {"kwargs": {"icon": icons.stats_button_icon, "tooltip": "Статистика"}},
}


class LeftMenu(VerticalLayout):
    def __init__(self, parent):
        self.buttons: dict[buttons.LeftMenuBaseIconButton] = {}
        self.button_names = list(BUTTONS_CONFIG.keys())
        super().__init__(parent=parent)

    def make(self):
        self.init_buttons()

        self.setStyleSheet(str(LEFT_MENU_STYLESHEET))
        self.setFixedWidth(int(LEFT_MENU_STYLESHEET['width']))
        self.set_content_margins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        for button in self.buttons.values():
            self.add_widget(button, alignment=QtCore.Qt.AlignTop)

    def init_buttons(self):
        self.buttons = {
            name: buttons.LeftMenuBaseIconButton(self, **kwargs_["kwargs"]) for name, kwargs_ in BUTTONS_CONFIG.items()
        }

        self.buttons["menu"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_menu.emit)
        self.buttons["enter_data"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_enter_data.emit)
        self.buttons["parameters"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_parameters.emit)
        self.buttons["trajectory"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_trajectory.emit)
        self.buttons["tnd"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_tnd.emit)
        self.buttons["mask_group"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_mask_group.emit)
        self.buttons["custom_graph"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_custom_graph.emit)
        self.buttons["stats"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_stats.emit)
