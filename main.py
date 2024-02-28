import sys

from PySide6.QtWidgets import QApplication

from bin.gui.windows import MainWindow
from bin.storage import Storage


def main():
    Storage()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.make()

    app.exec()


if __name__ == "__main__":
    main()
