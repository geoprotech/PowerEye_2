from typing import Literal

from .base_powereye_exception import BasePowereyeException
from bin.storage import Storage


class VisiblePowereyeException(BasePowereyeException):
    def __init__(self, text: str, level: Literal["debug", "info", "warn", "error", "critical"] = "info") -> None:
        super().__init__(text, level)
        self.setup_storage_connection()

    def setup_storage_connection(self):
        Storage().set("visible_exception", self.text)
        Storage().emit("visible_exception")
