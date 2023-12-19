import sys

from Bin.Gui.Windows.MainWindow import MainWindow
from PySide6.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
