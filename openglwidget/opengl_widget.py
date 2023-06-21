from OpenGL.raw.GLU import gluPerspective
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication
from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL.GL import *


class MyOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rotate = 0.0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_rotation)
        self.timer.start(10)  # 设置定时器间隔为10ms

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glPushMatrix()

        glTranslatef(0.0, 0.0, -2.0)  # 平移
        glRotatef(self.rotate, 0.0, 1.0, 0.0)  # 绕y轴旋转
        glRotatef(self.rotate, 1.0, 0.0, 0.0)  # 绕x轴旋转

        glColor3f(0.0, 0.0, 1.0)

        self.draw_cube()

        glPopMatrix()

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect_ratio = width / height
        gluPerspective(45.0, aspect_ratio, 0.1, 10.0)
        glMatrixMode(GL_MODELVIEW)

    def update_rotation(self):
        self.rotate += 0.3
        self.update()

    def draw_cube(self):
        vertex_list = [
            (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, 0.5, -0.5),
            (-0.5, -0.5, 0.5),
            (0.5, -0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, 0.5)
        ]

        index_list = [
            (0, 1),
            (2, 3),
            (4, 5),
            (6, 7),
            (0, 2),
            (1, 3),
            (4, 6),
            (5, 7),
            (0, 4),
            (1, 5),
            (7, 3),
            (2, 6)
        ]

        glBegin(GL_LINES)
        for index_pair in index_list:
            for i in range(2):
                vertex_index = index_pair[i]
                glVertex3fv(vertex_list[vertex_index])
        glEnd()


if __name__ == '__main__':
    app = QApplication([])
    window = MyOpenGLWidget()
    window.resize(800, 600)
    window.show()
    app.exec()
