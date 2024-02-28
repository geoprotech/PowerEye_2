from typing import Any, Literal

import PySide6.QtCore as QtCore

from bin.exceptions import StorageException


class Storage(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._data: dict[str : dict[Literal["value"] : Any, Literal["signals"] : list[QtCore.Signal]]] = {}
            cls._instance = object.__new__(cls)
        return cls._instance

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
            raise StorageException(f"Can't find signal'{signal.__name__}' for key '{key}'")

        return self._data[key]["signals"].remove(signal)

    def set(self, key: str, data: Any) -> None:
        if key in self._data:
            self._data[key]["value"] = data
        else:
            self._data[key] = {"value": data, "signals": []}

    def get(self, key: str) -> Any:
        if key not in self._data:
            raise StorageException(f"No key found: '{key}'")

        if not self._data[key]["value"]:
            raise StorageException(f"No comparable data for key: {key}")

        return self._data[key]["value"]

    def clear(self, key: str) -> None:
        if key not in self._data:
            raise StorageException(f"No key found: '{key}'")

        self._data[key]["value"] = None

    def isolate(self, key: str) -> None:
        if key not in self._data:
            raise StorageException(f"No key found: '{key}'")

        self._data[key]["signals"] = []

    def remove(self, key: str) -> None:
        if key not in self._data:
            raise StorageException(f"No key found: '{key}'")

        self._data.pop(key)
