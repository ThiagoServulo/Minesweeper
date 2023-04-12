from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon


class Icon(QIcon):
    def __init__(self):
        super().__init__()
        self.icon_number_1 = QIcon()
        self.icon_number_1.addFile("numero_1.jpg", QSize(), QIcon.Normal, QIcon.Off)
        #self.icon_number_1.actualSize(size=QSize(30, 30))

    def get_icon_number_1(self):
        return self.icon_number_1
