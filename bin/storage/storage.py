from typing import Any, Literal

import PySide6.QtCore as QtCore

from bin.exceptions import StorageException


class Storage(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self._data: dict[str : dict[Literal["value"] : Any, Literal["signals"] : QtCore.Signal]] = {}

    def emit(self, key: str):
        if key not in self._data:
            raise StorageException(f"No key found: {key}.")

        if len(self._data[key]["signals"]) == 0:
            raise StorageException(f"No comparable signal found for key: {key}.")

        for signal in self._data[key]["signals"]:
            signal.emit()

    def connect(self, key: str, signal: QtCore.Signal) -> None:
        if key in self._data:
            self._data[key]["signals"].append(signal)
        else:
            self._data[key] = {"value": None, "signals": [signal]}

    def disconnect(self, key: str, signal: QtCore.Signal) -> QtCore.Signal:
        if key not in self._data:
            raise StorageException(f"No key found: '{key}'.")

        if len(self._data[key]["signals"]) == 0:
            raise StorageException(f"No any signals found for key: '{key}'.")

        if signal not in self._data[key]["signals"]:
            raise StorageException(f"Can't find '{signal.__name__}' for key '{key}'")

        return self._data[key]["signals"].remove(signal)

    def push(self, key: str, data: Any) -> None:
        if key in self._data:
            self._data[key]["value"] = data
        else:
            self._data[key] = {"value": data, "signals": []}

    def pull(self, key: str) -> Any:
        if key not in self._data:
            raise StorageException(f"No key found: '{key}'")

        if not self._data[key]["value"]:
            raise StorageException(f"No comparable data for key: {key}")

        return self._data[key]["value"]


storage = Storage()


if __name__ == "__main__":
    storage.push("test_field", "test_value")
    a = storage.pull("test_field")
    print(a)
