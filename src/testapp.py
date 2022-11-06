import sys

from PyQt5.QtWidgets import *


class mywidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("hello world")
        self.setupUI()

    def setupUI(self):
        self.hlayout = QVBoxLayout()
        self.btn1 = QPushButton("btn1")
        self.btn2 = QPushButton("btn2")
        self.btn3 = QPushButton("btn3")

        self.hlayout.setSpacing(0)
        self.hlayout.setContentsMargins(0, 0, 0, 0)

        self.hlayout.addWidget(self.btn1)

        self.hlayout.addWidget(self.btn2)

        self.hlayout.addWidget(self.btn3)
        self.hlayout.addStretch()
        bottompart = QHBoxLayout()
        self.hlayout.addLayout(bottompart)
        self.hlayout.addSpacing(16)
        self.ok = QPushButton("OK")
        self.cancel = QPushButton("Cancel")
        bottompart.addStretch()
        bottompart.addWidget(self.ok)
        bottompart.addWidget(self.cancel)
        self.setLayout(self.hlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mywidget()

    window.resize(300, 200)
    window.move(250, 200)
    window.setWindowTitle("你好啊")
    window.show()
    sys.exit(app.exec_())
