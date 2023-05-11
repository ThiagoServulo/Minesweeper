from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from typing import Literal


class Icon(QIcon):
    def __init__(self):
        """
        Constructor
        """
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
        self.icon_gray = QIcon()
        self.icon_gray.addFile("images/gray2.jpg", QSize(), QIcon.Normal, QIcon.Off)

    def get_icon(self, value: Literal['b', 'B', '0', '1', '2', '3', '4', '5', '6', '7', '8', 'f', 'g']):
        """
        Get icons
        :param value: Code of the image
        :return: The icon based in the value parameter
        """
        if value == 'b':
            icon = self.icon_bomb
        elif value == 'B':
            icon = self.icon_bomb_exploded
        elif value == '0':
            icon = self.icon_blank
        elif value == '1':
            icon = self.icon_number_1
        elif value == '2':
            icon = self.icon_number_2
        elif value == '3':
            icon = self.icon_number_3
        elif value == '4':
            icon = self.icon_number_4
        elif value == '5':
            icon = self.icon_number_5
        elif value == '6':
            icon = self.icon_number_6
        elif value == '7':
            icon = self.icon_number_7
        elif value == '8':
            icon = self.icon_number_8
        elif value == 'f':
            icon = self.icon_flag
        elif value == 'g':
            icon = self.icon_gray
        else:
            raise "Invalid value"
        return icon
