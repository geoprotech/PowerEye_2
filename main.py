import sys

from PySide6.QtWidgets import QApplication

from bin.gui.windows import MainWindow
from bin.storage import Storage


def main():
    Storage()
    app = QApplication(sys.argv)
    Storage()
    window = MainWindow()

    app.exec()


if __name__ == "__main__":
    main()
