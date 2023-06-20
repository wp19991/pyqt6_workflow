import sys
import os
from PyQt6.QtWidgets import QApplication

os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


class App(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.windows = {}

    def run(self, pytest=False):
        from win.main_win import main_win
        self.windows["main_win"] = main_win()
        self.windows["main_win"].show()
        if not pytest:
            sys.exit(self.exec())


if __name__ == "__main__":
    App().run()
