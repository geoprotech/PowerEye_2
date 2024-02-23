from abc import abstractmethod
from typing import Literal

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QWidget

from .layouts_popup import HeaderLayoutPopUp
from bin.gui.decorators import init_protocol
from bin.gui.widgets import HorizontalLayout, VerticalLayout
from src.styles.components.windows import POP_UP_STYLESHEET


class BasePopUp(QDialog):
    layout_types_body = {"HBox": HorizontalLayout, "VBox": VerticalLayout}

    @init_protocol
    def __init__(
        self,
        parent: QWidget,
        layout_type_body: Literal[
            "HBox",
            "VBox",
        ],
        title: str,
        **kwargs
    ) -> None:
        self.__layout_type_body = layout_type_body
        self._parent = parent
        self.title = title

        super().__init__(parent=parent, **kwargs)

    def pre_setup(self) -> None:
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(POP_UP_STYLESHEET)

        self._layout_main = QVBoxLayout()  # noqa
        self._layout_main.setContentsMargins(0, 0, 0, 0)
        self._layout_main.setSpacing(0)

        self._header_layout_popup = HeaderLayoutPopUp(parent=self, title=self.title)  # noqa
        self._layout_main.addWidget(self._header_layout_popup, stretch=1)

        self._body_layout_popup = BasePopUp.layout_types_body.get(self.__layout_type_body)(self._parent)  # noqa
        self._body_layout_popup.set_content_margins(0, 0, 0, 0)
        self.set_spacing(0)
        self._layout_main.addWidget(self._body_layout_popup, stretch=1)

        self.setLayout(self._layout_main)

    @abstractmethod
    def make(self) -> None:
        """
        Function to create and configure layout. Must be overridden

            Example:
                self.add_widget(Color('red'))
        """

    def add_widget(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag or None = None) -> None:
        """
        adds a widget to the layout
        @param widget: QWidget
        @param stretch: int
        @param alignment: Qt.AlignmentFlag or None
        @return: None
        """

        # default alignment непонятно как определяется в Qt, поэтому сделал так
        if alignment:
            self._body_layout_popup.add_widget(widget, stretch, alignment)
        else:
            self._body_layout_popup.add_widget(widget, stretch)

    def set_content_margins(self, left: int, top: int, right: int, bottom: int) -> None:
        # self._layout_main.setContentsMargins(left, top, right, bottom)
        self._body_layout_popup.set_content_margins(left, top, right, bottom)

    def set_spacing(self, spacing: int) -> None:
        # self._layout_main.setSpacing(spacing)
        self._body_layout_popup.set_spacing(spacing)

    def set_geometry(self, x: int, y: int, width: int, height: int):
        self.move(x, y)
        self.resize(width, height)

    def show(self) -> None:
        self.exec()
