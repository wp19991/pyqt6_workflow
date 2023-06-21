from PyQt6.QtWidgets import QMainWindow

import openglwidget.opengl_widget
from ui.MainWindow import Ui_MainWindow as MainWindow


class main_win(QMainWindow, MainWindow):
    def __init__(self):
        super(main_win, self).__init__()
        self.setupUi(self)

        self.open = openglwidget.opengl_widget.MyOpenGLWidget()
        self.verticalLayout.addWidget(self.open)

