from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon


class Icon(QIcon):
    def __init__(self):
        super().__init__()
        self.icon_number_1 = QIcon()
        self.icon_number_1.addFile("images/number_1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_number_2 = QIcon()
        self.icon_number_2.addFile("images/number_2.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_number_3 = QIcon()
        self.icon_number_3.addFile("images/number_3.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_number_4 = QIcon()
        self.icon_number_4.addFile("images/number_4.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_number_5 = QIcon()
        self.icon_number_5.addFile("images/number_5.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_number_6 = QIcon()
        self.icon_number_6.addFile("images/number_6.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_number_7 = QIcon()
        self.icon_number_7.addFile("images/number_7.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_number_8 = QIcon()
        self.icon_number_8.addFile("images/number_8.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_blank = QIcon()
        self.icon_blank.addFile("images/blank.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_bomb = QIcon()
        self.icon_bomb.addFile("images/bomb.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_bomb_exploded = QIcon()
        self.icon_bomb_exploded.addFile("images/bomb_exploded.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_flag = QIcon()
        self.icon_flag.addFile("images/flag.jpg", QSize(), QIcon.Normal, QIcon.Off)

    def get_icon_number_1(self):
        return self.icon_number_1

    def get_icon_number_2(self):
        return self.icon_number_2

    def get_icon_number_3(self):
        return self.icon_number_3

    def get_icon_number_4(self):
        return self.icon_number_4

    def get_icon_number_5(self):
        return self.icon_number_5

    def get_icon_number_6(self):
        return self.icon_number_6

    def get_icon_number_7(self):
        return self.icon_number_7

    def get_icon_number_8(self):
        return self.icon_number_8

    def get_icon_blank(self):
        return self.icon_blank

    def get_icon_bomb(self):
        return self.icon_bomb

    def get_icon_bomb_exploded(self):
        return self.icon_bomb_exploded

    def get_icon_flag(self):
        return self.icon_flag
