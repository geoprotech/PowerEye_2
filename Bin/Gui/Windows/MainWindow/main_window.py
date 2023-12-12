from PySide6.QtWidgets import QMainWindow, QLabel

from Src.Style.stylesheet import BASE_STYLESHEET, MAIN_WINDOW_HEADER_STYLESHEET


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(int(BASE_STYLESHEET["geometry"].split("x")[0]),
                         int(BASE_STYLESHEET["geometry"].split("x")[1]),
                         int(BASE_STYLESHEET["geometry"].split("x")[2]),
                         int(BASE_STYLESHEET["geometry"].split("x")[3]))

        self.setStyleSheet(f"background-color: {BASE_STYLESHEET['background-color']};"
                           f"font-family: {BASE_STYLESHEET['font-family']};"
                           f"font: {BASE_STYLESHEET['font']};")

        self.setWindowTitle("PowerEye 2.0")
        self.header = QLabel(self)
        self.header.setStyleSheet(f"background-color: {MAIN_WINDOW_HEADER_STYLESHEET['background-color']};"
                                  f"font: {MAIN_WINDOW_HEADER_STYLESHEET['font']};"
                                  f"font-weight: {MAIN_WINDOW_HEADER_STYLESHEET['font-weight']};")
        self.header.setGeometry(0, 0, self.width() // 2, self.height() // 100 * 10)
        self.header.setText("PowerEye")

        self.header.setScaledContents(True)  # ???
