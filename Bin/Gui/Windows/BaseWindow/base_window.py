from Src.Style.stylesheet import BASE_STYLESHEET

from PySide6.QtWidgets import QWidget


class BaseWindow(QWidget):
    def __init__(self, title: str = "Window", geometry: str = None):
        super(BaseWindow, self).__init__()
        self.setWindowTitle(title)
        if geometry:
            self.setGeometry(int(geometry.split("x")[0]),
                             int(geometry.split("x")[0]),
                             int(geometry.split("x")[0]),
                             int(geometry.split("x")[0]))
        else:
            self.setGeometry(int(BASE_STYLESHEET["geometry"].split("x")[0]) // 2,
                             int(BASE_STYLESHEET["geometry"].split("x")[1]) // 2,
                             int(BASE_STYLESHEET["geometry"].split("x")[2]) // 2,
                             int(BASE_STYLESHEET["geometry"].split("x")[3]) // 2)

        self.setStyleSheet(f"background-color: {BASE_STYLESHEET['background-color']};"
                           f"font-family: {BASE_STYLESHEET['font-family']};"
                           f"font: {BASE_STYLESHEET['font']};")
