from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Icon import Icon


class Button(QPushButton):
    def __init__(self, widget, rect):
        super().__init__()
        self.button = QPushButton(widget)
        self.button.setGeometry(rect)
        self.icons = Icon()
        self.value = '0'
        self.icon = ""
        self.button.clicked.connect(self.show_image)

    def show_image(self):
        if self.value == 'b':
            self.icon = self.icons.get_icon_bomb()
        elif self.value == 'B':
            self.icon = self.icons.get_icon_bomb_exploded()
        elif self.value == '0':
            self.icon = self.icons.get_icon_blank()
        elif self.value == '1':
            self.icon = self.icons.get_icon_number_1()
        elif self.value == '2':
            self.icon = self.icons.get_icon_number_2()
        elif self.value == '3':
            self.icon = self.icons.get_icon_number_3()
        elif self.value == '4':
            self.icon = self.icons.get_icon_number_4()
        elif self.value == '5':
            self.icon = self.icons.get_icon_number_5()
        elif self.value == '6':
            self.icon = self.icons.get_icon_number_6()
        elif self.value == '7':
            self.icon = self.icons.get_icon_number_7()
        elif self.value == '8':
            self.icon = self.icons.get_icon_number_8()
        else:
            raise "Invalid value"
        self.button.setIcon(self.icon)
        self.button.setIconSize(QSize(30, 30))

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

