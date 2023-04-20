
from PySide2.QtWidgets import *


class ButtonFlag(QPushButton):
    def __init__(self, widget, rect):
        super().__init__()
        self.button = QPushButton(widget)
        self.button.setGeometry(rect)
        self.flag = False
        self.button.clicked.connect(self.toggle_flag)

    def toggle_flag(self):
        self.flag = True if self.flag == False else False
        print(self.flag)

    def get_flag(self):
        return self.flag
