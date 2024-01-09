from . import BasePowereyeException


class StylesheetException(BasePowereyeException):
    def __init__(self, text: str, level: str) -> None:
        super(StylesheetException, self).__init__(text, level)
