class LayoutException(Exception):
    def __init__(self, text: str, level: str) -> None:
        super(LayoutException, self).__init__(text)
        self.text = text
        self.level = level

    def __str__(self) -> str:
        return f"{self.level}: {self.text}"
