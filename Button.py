from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Button(QPushButton):
    def __init__(self, widget, rect):
        super().__init__()
        self.button = QPushButton(widget)
        self.button.setGeometry(rect)

    def define_image(self, icon):
        self.button.setIcon(icon)
        self.button.setIconSize(QSize(30, 30))
