import sys

from PySide6.QtWidgets import QApplication

from bin.gui.windows import MainWindow
from bin.storage import Storage


def main():
    app = QApplication(sys.argv)
    Storage()
    window = MainWindow()
    window.make()

    app.exec()


if __name__ == "__main__":
    main()
