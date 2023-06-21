from PyQt6.QtWidgets import QApplication
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt6.QtGui import QPainter
from OpenGL.GL import *


class MyOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)

        # 绘制彩色三角形
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.0, 0.0)  # 红色
        glVertex3f(0.0, 0.5, 0.0)
        glColor3f(0.0, 1.0, 0.0)  # 绿色
        glVertex3f(-0.5, -0.5, 0.0)
        glColor3f(0.0, 0.0, 1.0)  # 蓝色
        glVertex3f(0.5, -0.5, 0.0)
        glEnd()

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)

    def paintEvent(self, event):
        self.makeCurrent()
        painter = QPainter(self)
        self.paintGL()
        painter.end()
        self.doneCurrent()


if __name__ == '__main__':
    app = QApplication([])
    window = MyOpenGLWidget()
    window.resize(800, 600)
    window.show()
    app.exec()
