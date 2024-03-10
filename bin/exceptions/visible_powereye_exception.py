from typing import Literal

from . import BasePowereyeException


class VisiblePowereyeException(BasePowereyeException):
    def __init__(self, text: str, level: Literal["debug", "info", "warn", "error", "critical"]) -> None:
        super(VisiblePowereyeException, self).__init__(text, level)
        self._create_error_window()

    def _create_error_window(self) -> None:
        # create error window(use BaseWindow class)
        pass
