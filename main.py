import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.circles)
        self.draw = False

    def circles(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        if self.draw:
            for i in range(10):
                d = random.randint(5, 75)
                qp.drawEllipse(random.randint(0, self.width() - d),
                               random.randint(0, self.height() - d), d, d)


app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
