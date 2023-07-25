import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_MainWindow

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()

    sys.exit(app.exec())
