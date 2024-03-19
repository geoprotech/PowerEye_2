from PySide6.QtCore import QObject, Signal

from bin.gui.windows import WarningPopUp
from bin.storage import Storage


class VisibleExceptionHandler(QObject):
    _instance = None

    def __new__(cls):
        if not isinstance(cls._instance, cls):
            cls.storage_signal = Signal()
            cls._instance = super(VisibleExceptionHandler, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.storage_signal.connect(self.on_emit)
        Storage().connect("visible_exception", self.storage_signal)

    def on_emit(self):
        WarningPopUp(Storage().get('visible_exception'), 'Warning')
