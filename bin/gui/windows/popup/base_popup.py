from abc import abstractmethod
from typing import Literal

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QWidget

from bin.gui.decorators import init_protocol
from bin.gui.widgets import BaseLayout, HorizontalLayout, VerticalLayout
from bin.gui.widgets.layouts.popup import PopUpHeaderLayout
from src.styles.components.windows import DEFAULT_POP_UP_STYLESHEET


class BasePopUp(QDialog):
    """
    brief:

     self contain:
            -------------------------------------------
            |            header_layout                 |
            -------------------------------------------
            |            body_layout                  |
            -------------------------------------------


    @return:
    """

    body_layout_types = {"HBox": HorizontalLayout, "VBox": VerticalLayout}

    @init_protocol
    def __init__(self, parent: QWidget, body_layout: Literal["HBox", "VBox"], title: str or None, **kwargs) -> None:
        self._parent = parent
        self.title = title
        self._main_layout: QVBoxLayout
        self._header_layout: BaseLayout
        self._body_layout: BaseLayout = BasePopUp.body_layout_types.get(body_layout, "VBox")(self._parent)

        super().__init__(parent=parent, **kwargs)

    def pre_setup(self) -> None:
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet(DEFAULT_POP_UP_STYLESHEET)

        self._main_layout = QVBoxLayout()  # noqa
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.setSpacing(0)

        self._header_layout = PopUpHeaderLayout(parent=self, title=self.title)  # noqa
        self._main_layout.addWidget(self._header_layout)

        self._body_layout.set_content_margins(0, 0, 0, 0)
        self._main_layout.addWidget(self._body_layout)

        self.set_spacing(0)
        self.setLayout(self._main_layout)

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
            self._body_layout.add_widget(widget, stretch, alignment)
        else:
            self._body_layout.add_widget(widget, stretch)

    def set_content_margins(self, left: int, top: int, right: int, bottom: int) -> None:
        self._body_layout.set_content_margins(left, top, right, bottom)

    def set_spacing(self, spacing: int) -> None:
        self._body_layout.set_spacing(spacing)

    def show(self) -> None:
        self.exec()
