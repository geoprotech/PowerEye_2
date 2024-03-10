from typing import Literal

from . import BasePowereyeException


class StylesheetException(BasePowereyeException):
    def __init__(self, text: str, level: Literal["debug", "info", "warn", "error", "critical"]) -> None:
        super(StylesheetException, self).__init__(text, level)
