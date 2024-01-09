from . import BasePowereyeException


class VisiblePowereyeException(BasePowereyeException):
    def __init__(self, text: str, level: str) -> None:
        super(VisiblePowereyeException, self).__init__(text, level)
        self._create_error_window()

    def _create_error_window(self):
        # create error window(use BaseWindow class)
        pass
