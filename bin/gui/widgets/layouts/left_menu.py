from typing import Dict

import PySide6.QtCore as QtCore
from PySide6.QtCore import QPropertyAnimation, QSize

import src.icons as icons
import bin.gui.widgets.buttons as buttons
from .base_vertical_layout import VerticalLayout
from .main_workspace import MainWorkspaceLayout
from src.styles.components.widgets import LEFT_MENU_HOVER_STYLESHEET


BUTTONS_CONFIG = {
    "menu": {"kwargs": {"icon": icons.menu_button_icon, "tooltip": "Меню", "text": "Меню"}},
    "enter_data": {"kwargs": {"icon": icons.enter_data_button_icon, "tooltip": "Данные", "text": "Данные"}},
    "parameters": {"kwargs": {"icon": icons.parameters_button_icon, "tooltip": "Параметры", "text": "Параметры"}},
    "trajectory": {"kwargs": {"icon": icons.trajectory_button_icon, "tooltip": "Траектория", "text": "Траектория"}},
    "tnd": {"kwargs": {"icon": icons.tnd_button_icon, "tooltip": "T&D модель", "text": "T&D модель"}},
    "mask_group": {
        "kwargs": {"icon": icons.mask_group_button_icon, "tooltip": "Дифф. подлипания", "text": "Дифф. подлипания"}
    },
    "custom_graph": {
        "kwargs": {
            "icon": icons.custom_graph_button_icon,
            "tooltip": "Пользовательский график",
            "text": "Пользовательский график",
        }
    },
    "stats": {"kwargs": {"icon": icons.stats_button_icon, "tooltip": "Статистика", "text": "Статистика"}},
}

INITIAL_GEOMETRY = {"x": 0, "y": 45, "width": 60, "height": 800}

ENLARGED_GEOMETRY = {"x": 0, "y": 45, "width": 300, "height": 800}

ANIMATION_DURATION = 250  # ms


class LeftMenu(VerticalLayout):
    def __init__(self, parent):
        self.buttons: Dict[buttons.LeftMenuIconButton] = {}
        self.button_names = list(BUTTONS_CONFIG.keys())

        self.__enlarge_animation: QPropertyAnimation
        self.__hide_animation: QPropertyAnimation

        self.maximized = False  # initial state: True if maximized
        self.initial_geometry = INITIAL_GEOMETRY
        self.enlarged_geometry = ENLARGED_GEOMETRY
        super().__init__(parent=parent)

    def make(self):
        # initialize size animations
        self.__enlarge_animation = QPropertyAnimation(self, b"size")
        self.__hide_animation = QPropertyAnimation(self, b"size")

        self.setStyleSheet(LEFT_MENU_HOVER_STYLESHEET)
        self.set_content_margins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        # geometry should be initialized here cause it not static
        self.setGeometry(*list(INITIAL_GEOMETRY.values()))

        self.__init_animation()
        self.init_buttons()

        for button in self.buttons.values():
            self.add_widget(button, alignment=QtCore.Qt.AlignTop)  # noqa

    def init_buttons(self):
        self.buttons = {
            name: buttons.LeftMenuIconButton(self, **kwargs_["kwargs"]) for name, kwargs_ in BUTTONS_CONFIG.items()
        }

        self.buttons["menu"].add_onclick_event(self.start_animation)
        self.buttons["enter_data"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_enter_data.emit)
        self.buttons["parameters"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_parameters.emit)
        self.buttons["trajectory"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_trajectory.emit)
        self.buttons["tnd"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_tnd.emit)
        self.buttons["mask_group"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_mask_group.emit)
        self.buttons["custom_graph"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_custom_graph.emit)
        self.buttons["stats"].add_onclick_event(MainWorkspaceLayout.instance.switch_to_stats.emit)

    def __init_animation(self):
        # setup enlarge animation
        self.__enlarge_animation.setDuration(ANIMATION_DURATION)  # Длительность анимации в миллисекундах
        self.__enlarge_animation.setStartValue(QSize(self.initial_geometry["width"], self.initial_geometry["height"]))
        self.__enlarge_animation.setEndValue(
            QSize(self.enlarged_geometry["width"], self.enlarged_geometry["height"])
        )  # Сдвиг влево на 100 пикселей

        # setup hide animation
        self.__hide_animation.setDuration(ANIMATION_DURATION)  # Длительность анимации в миллисекундах
        self.__hide_animation.setStartValue(QSize(self.enlarged_geometry["width"], self.enlarged_geometry["height"]))
        self.__hide_animation.setEndValue(
            QSize(self.initial_geometry["width"], self.initial_geometry["height"])
        )  # Сдвиг влево на 100 пикселей

    def start_animation(self):
        """
        start hide or enlarge animation (depend on maximized state)
        @return:
        """
        self.start_hide_animation() if self.maximized else self.start_enlarge_animation()

    def start_enlarge_animation(self):
        self.__enlarge_animation.start()
        self.maximized = True

    def start_hide_animation(self):
        self.__hide_animation.start()
        self.maximized = False

    def leaveEvent(self, event):  # noqa
        if self.maximized:
            self.start_hide_animation()

    def recalc_geometry(self):
        """
        TODO: после реализации ресайза тут будет пересчет self.initial_geometry и self.enlarged_geometry
        @return:
        """
