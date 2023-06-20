from PyQt6.QtWidgets import QMainWindow
from ui.MainWindow import Ui_MainWindow as MainWindow


class main_win(QMainWindow, MainWindow):
    def __init__(self):
        super(main_win, self).__init__()
        self.setupUi(self)
