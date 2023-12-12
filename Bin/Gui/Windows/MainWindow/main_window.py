from PySide6.QtWidgets import QHBoxLayout, QLabel, QMainWindow

from Src.Style.stylesheet import BASE_STYLESHEET, MAIN_WINDOW_HEADER_STYLESHEET


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(*BASE_STYLESHEET.geometry())
        self.setStyleSheet(repr(BASE_STYLESHEET))

        self.setWindowTitle("PowerEye 2.0")
        self.header = QLabel(self)

        self.header.setStyleSheet(repr(MAIN_WINDOW_HEADER_STYLESHEET))

        self.header.setGeometry(
            0, 0, self.width() // 2, self.height() // 100 * 10
        )
        self.header.setText("PowerEye")
        self.header.setFixedHeight(80)
        self.box_layout = QHBoxLayout()
        self.box_layout.addWidget(self.header)
        self.setLayout(self.box_layout)

        self.setCentralWidget(self.header)
