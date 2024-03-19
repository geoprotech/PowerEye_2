import sys

from PySide6.QtWidgets import QApplication

from bin.exceptions.visible_exception_handler import ExceptionHandler
from bin.gui.windows import MainWindow
from bin.storage import Storage


def main():
    app = QApplication(sys.argv)
    Storage()
    ExceptionHandler()
    window = MainWindow()

    app.exec()


if __name__ == "__main__":
    main()
