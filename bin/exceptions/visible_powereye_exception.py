from .base_powereye_exception import BasePowereyeException
from bin.storage import Storage


class VisiblePowereyeException(BasePowereyeException):
    def __init__(self, text: str, level: str) -> None:
        super().__init__(text, level)
        self.text = text
        self.handler()

    def handler(self):
        Storage().set("visible_exception", self.text)
        Storage().emit("visible_exception")
