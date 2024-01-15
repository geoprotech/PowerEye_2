import sys

from PySide6.QtWidgets import QApplication

from bin.gui.windows import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.generate()

    app.exec()


if __name__ == "__main__":
    main()
