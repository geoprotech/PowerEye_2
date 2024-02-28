from typing import Literal


class BasePowereyeException(Exception):
    def __init__(self, text: str, level: Literal["debug", "info", "warn", "error", "critical"] = "info") -> None:
        super().__init__(text)
        self.text = text
        self.level = level

    def __str__(self) -> str:
        return f"{self.level}: {self.text}"
