import sys
from random import randint
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Button import Button
from ButtonFlag import ButtonFlag
from Icon import Icon


class Ui_MainWindow(object):
    # Constants
    LENGTH_AXIS_X = 15
    LENGTH_AXIS_Y = 15
    QUANTITY_BOMBS = 40

    def __init__(self):
        self.centralwidget = QWidget()
        self.icons = Icon()
        # First line
        #self.pushButtonA1 = Button()
        #self.pushButtonA2 = Button()
        #self.pushButtonA3 = Button()
        self.pushButtonA4 = Button()
        self.pushButtonA5 = Button()
        self.pushButtonA6 = Button()
        self.pushButtonA7 = Button()
        self.pushButtonA8 = Button()
        self.pushButtonA9 = Button()
        self.pushButtonA10 = Button()
        self.pushButtonA11 = Button()
        self.pushButtonA12 = Button()
        self.pushButtonA13 = Button()
        self.pushButtonA14 = Button()
        self.pushButtonA15 = Button()
        # Second line
        #self.pushButtonB1 = Button()
        #self.pushButtonB2 = Button()
        #self.pushButtonB3 = Button()
        self.pushButtonB4 = Button()
        self.pushButtonB5 = Button()
        self.pushButtonB6 = Button()
        self.pushButtonB7 = Button()
        self.pushButtonB8 = Button()
        self.pushButtonB9 = Button()
        self.pushButtonB10 = Button()
        self.pushButtonB11 = Button()
        self.pushButtonB12 = Button()
        self.pushButtonB13 = Button()
        self.pushButtonB14 = Button()
        self.pushButtonB15 = Button()
        # Third line
        # self.pushButtonC1 = Button()
        # self.pushButtonC2 = Button()
        # self.pushButtonC3 = Button()
        self.pushButtonC4 = Button()
        self.pushButtonC5 = Button()
        self.pushButtonC6 = Button()
        self.pushButtonC7 = Button()
        self.pushButtonC8 = Button()
        self.pushButtonC9 = Button()
        self.pushButtonC10 = Button()
        self.pushButtonC11 = Button()
        self.pushButtonC12 = Button()
        self.pushButtonC13 = Button()
        self.pushButtonC14 = Button()
        self.pushButtonC15 = Button()
        # Fourth line
        self.pushButtonD1 = Button()
        self.pushButtonD2 = Button()
        self.pushButtonD3 = Button()
        self.pushButtonD4 = Button()
        self.pushButtonD5 = Button()
        self.pushButtonD6 = Button()
        self.pushButtonD7 = Button()
        self.pushButtonD8 = Button()
        self.pushButtonD9 = Button()
        self.pushButtonD10 = Button()
        self.pushButtonD11 = Button()
        self.pushButtonD12 = Button()
        self.pushButtonD13 = Button()
        self.pushButtonD14 = Button()
        self.pushButtonD15 = Button()
        # Fiveth line
        self.pushButtonE1 = Button()
        self.pushButtonE2 = Button()
        self.pushButtonE3 = Button()
        self.pushButtonE4 = Button()
        self.pushButtonE5 = Button()
        self.pushButtonE6 = Button()
        self.pushButtonE7 = Button()
        self.pushButtonE8 = Button()
        self.pushButtonE9 = Button()
        self.pushButtonE10 = Button()
        self.pushButtonE11 = Button()
        self.pushButtonE12 = Button()
        self.pushButtonE13 = Button()
        self.pushButtonE14 = Button()
        self.pushButtonE15 = Button()
        # Sixth line
        self.pushButtonF1 = Button()
        self.pushButtonF2 = Button()
        self.pushButtonF3 = Button()
        self.pushButtonF4 = Button()
        self.pushButtonF5 = Button()
        self.pushButtonF6 = Button()
        self.pushButtonF7 = Button()
        self.pushButtonF8 = Button()
        self.pushButtonF9 = Button()
        self.pushButtonF10 = Button()
        self.pushButtonF11 = Button()
        self.pushButtonF12 = Button()
        self.pushButtonF13 = Button()
        self.pushButtonF14 = Button()
        self.pushButtonF15 = Button()
        # Seventh line
        self.pushButtonG1 = Button()
        self.pushButtonG2 = Button()
        self.pushButtonG3 = Button()
        self.pushButtonG4 = Button()
        self.pushButtonG5 = Button()
        self.pushButtonG6 = Button()
        self.pushButtonG7 = Button()
        self.pushButtonG8 = Button()
        self.pushButtonG9 = Button()
        self.pushButtonG10 = Button()
        self.pushButtonG11 = Button()
        self.pushButtonG12 = Button()
        self.pushButtonG13 = Button()
        self.pushButtonG14 = Button()
        self.pushButtonG15 = Button()
        # Eighth line
        self.pushButtonH1 = Button()
        self.pushButtonH2 = Button()
        self.pushButtonH3 = Button()
        self.pushButtonH4 = Button()
        self.pushButtonH5 = Button()
        self.pushButtonH6 = Button()
        self.pushButtonH7 = Button()
        self.pushButtonH8 = Button()
        self.pushButtonH9 = Button()
        self.pushButtonH10 = Button()
        self.pushButtonH11 = Button()
        self.pushButtonH12 = Button()
        self.pushButtonH13 = Button()
        self.pushButtonH14 = Button()
        self.pushButtonH15 = Button()
        # Nineth line
        self.pushButtonI1 = Button()
        self.pushButtonI2 = Button()
        self.pushButtonI3 = Button()
        self.pushButtonI4 = Button()
        self.pushButtonI5 = Button()
        self.pushButtonI6 = Button()
        self.pushButtonI7 = Button()
        self.pushButtonI8 = Button()
        self.pushButtonI9 = Button()
        self.pushButtonI10 = Button()
        self.pushButtonI11 = Button()
        self.pushButtonI12 = Button()
        self.pushButtonI13 = Button()
        self.pushButtonI14 = Button()
        self.pushButtonI15 = Button()
        # Tenth line
        self.pushButtonJ1 = Button()
        self.pushButtonJ2 = Button()
        self.pushButtonJ3 = Button()
        self.pushButtonJ4 = Button()
        self.pushButtonJ5 = Button()
        self.pushButtonJ6 = Button()
        self.pushButtonJ7 = Button()
        self.pushButtonJ8 = Button()
        self.pushButtonJ9 = Button()
        self.pushButtonJ10 = Button()
        self.pushButtonJ11 = Button()
        self.pushButtonJ12 = Button()
        self.pushButtonJ13 = Button()
        self.pushButtonJ14 = Button()
        self.pushButtonJ15 = Button()
        # Eleventh line
        self.pushButtonK1 = Button()
        self.pushButtonK2 = Button()
        self.pushButtonK3 = Button()
        self.pushButtonK4 = Button()
        self.pushButtonK5 = Button()
        self.pushButtonK6 = Button()
        self.pushButtonK7 = Button()
        self.pushButtonK8 = Button()
        self.pushButtonK9 = Button()
        self.pushButtonK10 = Button()
        self.pushButtonK11 = Button()
        self.pushButtonK12 = Button()
        self.pushButtonK13 = Button()
        self.pushButtonK14 = Button()
        self.pushButtonK15 = Button()
        # Twelveth line
        self.pushButtonL1 = Button()
        self.pushButtonL2 = Button()
        self.pushButtonL3 = Button()
        self.pushButtonL4 = Button()
        self.pushButtonL5 = Button()
        self.pushButtonL6 = Button()
        self.pushButtonL7 = Button()
        self.pushButtonL8 = Button()
        self.pushButtonL9 = Button()
        self.pushButtonL10 = Button()
        self.pushButtonL11 = Button()
        self.pushButtonL12 = Button()
        self.pushButtonL13 = Button()
        self.pushButtonL14 = Button()
        self.pushButtonL15 = Button()
        # Thirteenth line
        self.pushButtonM1 = Button()
        self.pushButtonM2 = Button()
        self.pushButtonM3 = Button()
        self.pushButtonM4 = Button()
        self.pushButtonM5 = Button()
        self.pushButtonM6 = Button()
        self.pushButtonM7 = Button()
        self.pushButtonM8 = Button()
        self.pushButtonM9 = Button()
        self.pushButtonM10 = Button()
        self.pushButtonM11 = Button()
        self.pushButtonM12 = Button()
        self.pushButtonM13 = Button()
        self.pushButtonM14 = Button()
        self.pushButtonM15 = Button()
        # Fourteenth line
        self.pushButtonN1 = Button()
        self.pushButtonN2 = Button()
        self.pushButtonN3 = Button()
        self.pushButtonN4 = Button()
        self.pushButtonN5 = Button()
        self.pushButtonN6 = Button()
        self.pushButtonN7 = Button()
        self.pushButtonN8 = Button()
        self.pushButtonN9 = Button()
        self.pushButtonN10 = Button()
        self.pushButtonN11 = Button()
        self.pushButtonN12 = Button()
        self.pushButtonN13 = Button()
        self.pushButtonN14 = Button()
        self.pushButtonN15 = Button()
        # Fiveteenth line
        self.pushButtonO1 = Button()
        self.pushButtonO2 = Button()
        self.pushButtonO3 = Button()
        self.pushButtonO4 = Button()
        self.pushButtonO5 = Button()
        self.pushButtonO6 = Button()
        self.pushButtonO7 = Button()
        self.pushButtonO8 = Button()
        self.pushButtonO9 = Button()
        self.pushButtonO10 = Button()
        self.pushButtonO11 = Button()
        self.pushButtonO12 = Button()
        self.pushButtonO13 = Button()
        self.pushButtonO14 = Button()
        self.pushButtonO15 = Button()
        # Create board
        self.board = []
        # Button flag
        self.pushButtonFlag = ButtonFlag()

    def create_board(self):
        self.board = \
            [[self.pushButtonA1, self.pushButtonA2, self.pushButtonA3, self.pushButtonA4, self.pushButtonA5,
              self.pushButtonA6, self.pushButtonA7, self.pushButtonA8, self.pushButtonA9, self.pushButtonA10,
              self.pushButtonA11, self.pushButtonA12, self.pushButtonA13, self.pushButtonA14, self.pushButtonA15],
             [self.pushButtonB1, self.pushButtonB2, self.pushButtonB3, self.pushButtonB4, self.pushButtonB5,
              self.pushButtonB6, self.pushButtonB7, self.pushButtonB8, self.pushButtonB9, self.pushButtonB10,
              self.pushButtonB11, self.pushButtonB12, self.pushButtonB13, self.pushButtonB14, self.pushButtonB15],
             [self.pushButtonC1, self.pushButtonC2, self.pushButtonC3, self.pushButtonC4, self.pushButtonC5,
              self.pushButtonC6, self.pushButtonC7, self.pushButtonC8, self.pushButtonC9, self.pushButtonC10,
              self.pushButtonC11, self.pushButtonC12, self.pushButtonC13, self.pushButtonC14, self.pushButtonC15],
             [self.pushButtonD1, self.pushButtonD2, self.pushButtonD3, self.pushButtonD4, self.pushButtonD5,
              self.pushButtonD6, self.pushButtonD7, self.pushButtonD8, self.pushButtonD9, self.pushButtonD10,
              self.pushButtonD11, self.pushButtonD12, self.pushButtonD13, self.pushButtonD14, self.pushButtonD15],
             [self.pushButtonE1, self.pushButtonE2, self.pushButtonE3, self.pushButtonE4, self.pushButtonE5,
              self.pushButtonE6, self.pushButtonE7, self.pushButtonE8, self.pushButtonE9, self.pushButtonE10,
              self.pushButtonE11, self.pushButtonE12, self.pushButtonE13, self.pushButtonE14, self.pushButtonE15],
             [self.pushButtonF1, self.pushButtonF2, self.pushButtonF3, self.pushButtonF4, self.pushButtonF5,
              self.pushButtonF6, self.pushButtonF7, self.pushButtonF8, self.pushButtonF9, self.pushButtonF10,
              self.pushButtonF11, self.pushButtonF12, self.pushButtonF13, self.pushButtonF14, self.pushButtonF15],
             [self.pushButtonG1, self.pushButtonG2, self.pushButtonG3, self.pushButtonG4, self.pushButtonG5,
              self.pushButtonG6, self.pushButtonG7, self.pushButtonG8, self.pushButtonG9, self.pushButtonG10,
              self.pushButtonG11, self.pushButtonG12, self.pushButtonG13, self.pushButtonG14, self.pushButtonG15],
             [self.pushButtonH1, self.pushButtonH2, self.pushButtonH3, self.pushButtonH4, self.pushButtonH5,
              self.pushButtonH6, self.pushButtonH7, self.pushButtonH8, self.pushButtonH9, self.pushButtonH10,
              self.pushButtonH11, self.pushButtonH12, self.pushButtonH13, self.pushButtonH14, self.pushButtonH15],
             [self.pushButtonI1, self.pushButtonI2, self.pushButtonI3, self.pushButtonI4, self.pushButtonI5,
              self.pushButtonI6, self.pushButtonI7, self.pushButtonI8, self.pushButtonI9, self.pushButtonI10,
              self.pushButtonI11, self.pushButtonI12, self.pushButtonI13, self.pushButtonI14, self.pushButtonI15],
             [self.pushButtonJ1, self.pushButtonJ2, self.pushButtonJ3, self.pushButtonJ4, self.pushButtonJ5,
              self.pushButtonJ6, self.pushButtonJ7, self.pushButtonJ8, self.pushButtonJ9, self.pushButtonJ10,
              self.pushButtonJ11, self.pushButtonJ12, self.pushButtonJ13, self.pushButtonJ14, self.pushButtonJ15],
             [self.pushButtonK1, self.pushButtonK2, self.pushButtonK3, self.pushButtonK4, self.pushButtonK5,
              self.pushButtonK6, self.pushButtonK7, self.pushButtonK8, self.pushButtonK9, self.pushButtonK10,
              self.pushButtonK11, self.pushButtonK12, self.pushButtonK13, self.pushButtonK14, self.pushButtonK15],
             [self.pushButtonL1, self.pushButtonL2, self.pushButtonL3, self.pushButtonL4, self.pushButtonL5,
              self.pushButtonL6, self.pushButtonL7, self.pushButtonL8, self.pushButtonL9, self.pushButtonL10,
              self.pushButtonL11, self.pushButtonL12, self.pushButtonL13, self.pushButtonL14, self.pushButtonL15],
             [self.pushButtonM1, self.pushButtonM2, self.pushButtonM3, self.pushButtonM4, self.pushButtonM5,
              self.pushButtonM6, self.pushButtonM7, self.pushButtonM8, self.pushButtonM9, self.pushButtonM10,
              self.pushButtonM11, self.pushButtonM12, self.pushButtonM13, self.pushButtonM14, self.pushButtonM15],
             [self.pushButtonN1, self.pushButtonN2, self.pushButtonN3, self.pushButtonN4, self.pushButtonN5,
              self.pushButtonN6, self.pushButtonN7, self.pushButtonN8, self.pushButtonN9, self.pushButtonN10,
              self.pushButtonN11, self.pushButtonN12, self.pushButtonN13, self.pushButtonN14, self.pushButtonN15],
             [self.pushButtonO1, self.pushButtonO2, self.pushButtonO3, self.pushButtonO4, self.pushButtonO5,
              self.pushButtonO6, self.pushButtonO7, self.pushButtonO8, self.pushButtonO9, self.pushButtonO10,
              self.pushButtonO11, self.pushButtonO12, self.pushButtonO13, self.pushButtonO14, self.pushButtonO15]
             ]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        # First line
        self.pushButtonA1 = QPushButton(self.centralwidget)
        self.pushButtonA1.setGeometry(QRect(10, 30, 30, 30))
        self.pushButtonA2 = QPushButton(self.centralwidget)
        self.pushButtonA2.setGeometry(QRect(40, 30, 30, 30))
        self.pushButtonA3 = QPushButton(self.centralwidget)
        self.pushButtonA3.setGeometry(QRect(70, 30, 30, 30))
        self.pushButtonA4 = QPushButton(self.centralwidget)
        self.pushButtonA4.setGeometry(QRect(100, 30, 30, 30))
        self.pushButtonA5 = QPushButton(self.centralwidget)
        self.pushButtonA5.setGeometry(QRect(130, 30, 30, 30))
        self.pushButtonA6 = QPushButton(self.centralwidget)
        self.pushButtonA6.setGeometry(QRect(160, 30, 30, 30))
        self.pushButtonA7 = QPushButton(self.centralwidget)
        self.pushButtonA7.setGeometry(QRect(190, 30, 30, 30))
        self.pushButtonA8 = QPushButton(self.centralwidget)
        self.pushButtonA8.setGeometry(QRect(220, 30, 30, 30))
        self.pushButtonA9 = QPushButton(self.centralwidget)
        self.pushButtonA9.setGeometry(QRect(250, 30, 30, 30))
        self.pushButtonA10 = QPushButton(self.centralwidget)
        self.pushButtonA10.setGeometry(QRect(280, 30, 30, 30))
        self.pushButtonA11 = QPushButton(self.centralwidget)
        self.pushButtonA11.setGeometry(QRect(310, 30, 30, 30))
        self.pushButtonA12 = QPushButton(self.centralwidget)
        self.pushButtonA12.setGeometry(QRect(340, 30, 30, 30))
        self.pushButtonA13 = QPushButton(self.centralwidget)
        self.pushButtonA13.setGeometry(QRect(370, 30, 30, 30))
        self.pushButtonA14 = QPushButton(self.centralwidget)
        self.pushButtonA14.setGeometry(QRect(400, 30, 30, 30))
        self.pushButtonA15 = QPushButton(self.centralwidget)
        self.pushButtonA15.setGeometry(QRect(430, 30, 30, 30))
        # Second line
        self.pushButtonB1 = QPushButton(self.centralwidget)
        self.pushButtonB1.setGeometry(QRect(10, 60, 30, 30))
        self.pushButtonB2 = QPushButton(self.centralwidget)
        self.pushButtonB2.setGeometry(QRect(40, 60, 30, 30))
        self.pushButtonB3 = QPushButton(self.centralwidget)
        self.pushButtonB3.setGeometry(QRect(70, 60, 30, 30))
        self.pushButtonB4 = QPushButton(self.centralwidget)
        self.pushButtonB4.setGeometry(QRect(100, 60, 30, 30))
        self.pushButtonB5 = QPushButton(self.centralwidget)
        self.pushButtonB5.setGeometry(QRect(130, 60, 30, 30))
        self.pushButtonB6 = QPushButton(self.centralwidget)
        self.pushButtonB6.setGeometry(QRect(160, 60, 30, 30))
        self.pushButtonB7 = QPushButton(self.centralwidget)
        self.pushButtonB7.setGeometry(QRect(190, 60, 30, 30))
        self.pushButtonB8 = QPushButton(self.centralwidget)
        self.pushButtonB8.setGeometry(QRect(220, 60, 30, 30))
        self.pushButtonB9 = QPushButton(self.centralwidget)
        self.pushButtonB9.setGeometry(QRect(250, 60, 30, 30))
        self.pushButtonB10 = QPushButton(self.centralwidget)
        self.pushButtonB10.setGeometry(QRect(280, 60, 30, 30))
        self.pushButtonB11 = QPushButton(self.centralwidget)
        self.pushButtonB11.setGeometry(QRect(310, 60, 30, 30))
        self.pushButtonB12 = QPushButton(self.centralwidget)
        self.pushButtonB12.setGeometry(QRect(340, 60, 30, 30))
        self.pushButtonB13 = QPushButton(self.centralwidget)
        self.pushButtonB13.setGeometry(QRect(370, 60, 30, 30))
        self.pushButtonB14 = QPushButton(self.centralwidget)
        self.pushButtonB14.setGeometry(QRect(400, 60, 30, 30))
        self.pushButtonB15 = QPushButton(self.centralwidget)
        self.pushButtonB15.setGeometry(QRect(430, 60, 30, 30))
        # Third line
        self.pushButtonC1 = QPushButton(self.centralwidget)
        self.pushButtonC1.setGeometry(QRect(10, 90, 30, 30))
        self.pushButtonC2 = QPushButton(self.centralwidget)
        self.pushButtonC2.setGeometry(QRect(40, 90, 30, 30))
        self.pushButtonC3 = QPushButton(self.centralwidget)
        self.pushButtonC3.setGeometry(QRect(70, 90, 30, 30))
        self.pushButtonC4 = QPushButton(self.centralwidget)
        self.pushButtonC4.setGeometry(QRect(100, 90, 30, 30))
        self.pushButtonC5 = QPushButton(self.centralwidget)
        self.pushButtonC5.setGeometry(QRect(130, 90, 30, 30))
        self.pushButtonC6 = QPushButton(self.centralwidget)
        self.pushButtonC6.setGeometry(QRect(160, 90, 30, 30))
        self.pushButtonC7 = QPushButton(self.centralwidget)
        self.pushButtonC7.setGeometry(QRect(190, 90, 30, 30))
        self.pushButtonC8 = QPushButton(self.centralwidget)
        self.pushButtonC8.setGeometry(QRect(220, 90, 30, 30))
        self.pushButtonC9 = QPushButton(self.centralwidget)
        self.pushButtonC9.setGeometry(QRect(250, 90, 30, 30))
        self.pushButtonC10 = QPushButton(self.centralwidget)
        self.pushButtonC10.setGeometry(QRect(280, 90, 30, 30))
        self.pushButtonC11 = QPushButton(self.centralwidget)
        self.pushButtonC11.setGeometry(QRect(310, 90, 30, 30))
        self.pushButtonC12 = QPushButton(self.centralwidget)
        self.pushButtonC12.setGeometry(QRect(340, 90, 30, 30))
        self.pushButtonC13 = QPushButton(self.centralwidget)
        self.pushButtonC13.setGeometry(QRect(370, 90, 30, 30))
        self.pushButtonC14 = QPushButton(self.centralwidget)
        self.pushButtonC14.setGeometry(QRect(400, 90, 30, 30))
        self.pushButtonC15 = QPushButton(self.centralwidget)
        self.pushButtonC15.setGeometry(QRect(430, 90, 30, 30))
        # Fourth line
        self.pushButtonD1 = QPushButton(self.centralwidget)
        self.pushButtonD1.setGeometry(QRect(10, 120, 30, 30))
        self.pushButtonD2 = QPushButton(self.centralwidget)
        self.pushButtonD2.setGeometry(QRect(40, 120, 30, 30))
        self.pushButtonD3 = QPushButton(self.centralwidget)
        self.pushButtonD3.setGeometry(QRect(70, 120, 30, 30))
        self.pushButtonD4 = QPushButton(self.centralwidget)
        self.pushButtonD4.setGeometry(QRect(100, 120, 30, 30))
        self.pushButtonD5 = QPushButton(self.centralwidget)
        self.pushButtonD5.setGeometry(QRect(130, 120, 30, 30))
        self.pushButtonD6 = QPushButton(self.centralwidget)
        self.pushButtonD6.setGeometry(QRect(160, 120, 30, 30))
        self.pushButtonD7 = QPushButton(self.centralwidget)
        self.pushButtonD7.setGeometry(QRect(190, 120, 30, 30))
        self.pushButtonD8 = QPushButton(self.centralwidget)
        self.pushButtonD8.setGeometry(QRect(220, 120, 30, 30))
        self.pushButtonD9 = QPushButton(self.centralwidget)
        self.pushButtonD9.setGeometry(QRect(250, 120, 30, 30))
        self.pushButtonD10 = QPushButton(self.centralwidget)
        self.pushButtonD10.setGeometry(QRect(280, 120, 30, 30))
        self.pushButtonD11 = QPushButton(self.centralwidget)
        self.pushButtonD11.setGeometry(QRect(310, 120, 30, 30))
        self.pushButtonD12 = QPushButton(self.centralwidget)
        self.pushButtonD12.setGeometry(QRect(340, 120, 30, 30))
        self.pushButtonD13 = QPushButton(self.centralwidget)
        self.pushButtonD13.setGeometry(QRect(370, 120, 30, 30))
        self.pushButtonD14 = QPushButton(self.centralwidget)
        self.pushButtonD14.setGeometry(QRect(400, 120, 30, 30))
        self.pushButtonD15 = QPushButton(self.centralwidget)
        self.pushButtonD15.setGeometry(QRect(430, 120, 30, 30))
        # Fiveth line
        self.pushButtonE1 = QPushButton(self.centralwidget)
        self.pushButtonE1.setGeometry(QRect(10, 150, 30, 30))
        self.pushButtonE2 = QPushButton(self.centralwidget)
        self.pushButtonE2.setGeometry(QRect(40, 150, 30, 30))
        self.pushButtonE3 = QPushButton(self.centralwidget)
        self.pushButtonE3.setGeometry(QRect(70, 150, 30, 30))
        self.pushButtonE4 = QPushButton(self.centralwidget)
        self.pushButtonE4.setGeometry(QRect(100, 150, 30, 30))
        self.pushButtonE5 = QPushButton(self.centralwidget)
        self.pushButtonE5.setGeometry(QRect(130, 150, 30, 30))
        self.pushButtonE6 = QPushButton(self.centralwidget)
        self.pushButtonE6.setGeometry(QRect(160, 150, 30, 30))
        self.pushButtonE7 = QPushButton(self.centralwidget)
        self.pushButtonE7.setGeometry(QRect(190, 150, 30, 30))
        self.pushButtonE8 = QPushButton(self.centralwidget)
        self.pushButtonE8.setGeometry(QRect(220, 150, 30, 30))
        self.pushButtonE9 = QPushButton(self.centralwidget)
        self.pushButtonE9.setGeometry(QRect(250, 150, 30, 30))
        self.pushButtonE10 = QPushButton(self.centralwidget)
        self.pushButtonE10.setGeometry(QRect(280, 150, 30, 30))
        self.pushButtonE11 = QPushButton(self.centralwidget)
        self.pushButtonE11.setGeometry(QRect(310, 150, 30, 30))
        self.pushButtonE12 = QPushButton(self.centralwidget)
        self.pushButtonE12.setGeometry(QRect(340, 150, 30, 30))
        self.pushButtonE13 = QPushButton(self.centralwidget)
        self.pushButtonE13.setGeometry(QRect(370, 150, 30, 30))
        self.pushButtonE14 = QPushButton(self.centralwidget)
        self.pushButtonE14.setGeometry(QRect(400, 150, 30, 30))
        self.pushButtonE15 = QPushButton(self.centralwidget)
        self.pushButtonE15.setGeometry(QRect(430, 150, 30, 30))
        # Sixth line
        self.pushButtonF1 = QPushButton(self.centralwidget)
        self.pushButtonF1.setGeometry(QRect(10, 180, 30, 30))
        self.pushButtonF2 = QPushButton(self.centralwidget)
        self.pushButtonF2.setGeometry(QRect(40, 180, 30, 30))
        self.pushButtonF3 = QPushButton(self.centralwidget)
        self.pushButtonF3.setGeometry(QRect(70, 180, 30, 30))
        self.pushButtonF4 = QPushButton(self.centralwidget)
        self.pushButtonF4.setGeometry(QRect(100, 180, 30, 30))
        self.pushButtonF5 = QPushButton(self.centralwidget)
        self.pushButtonF5.setGeometry(QRect(130, 180, 30, 30))
        self.pushButtonF6 = QPushButton(self.centralwidget)
        self.pushButtonF6.setGeometry(QRect(160, 180, 30, 30))
        self.pushButtonF7 = QPushButton(self.centralwidget)
        self.pushButtonF7.setGeometry(QRect(190, 180, 30, 30))
        self.pushButtonF8 = QPushButton(self.centralwidget)
        self.pushButtonF8.setGeometry(QRect(220, 180, 30, 30))
        self.pushButtonF9 = QPushButton(self.centralwidget)
        self.pushButtonF9.setGeometry(QRect(250, 180, 30, 30))
        self.pushButtonF10 = QPushButton(self.centralwidget)
        self.pushButtonF10.setGeometry(QRect(280, 180, 30, 30))
        self.pushButtonF11 = QPushButton(self.centralwidget)
        self.pushButtonF11.setGeometry(QRect(310, 180, 30, 30))
        self.pushButtonF12 = QPushButton(self.centralwidget)
        self.pushButtonF12.setGeometry(QRect(340, 180, 30, 30))
        self.pushButtonF13 = QPushButton(self.centralwidget)
        self.pushButtonF13.setGeometry(QRect(370, 180, 30, 30))
        self.pushButtonF14 = QPushButton(self.centralwidget)
        self.pushButtonF14.setGeometry(QRect(400, 180, 30, 30))
        self.pushButtonF15 = QPushButton(self.centralwidget)
        self.pushButtonF15.setGeometry(QRect(430, 180, 30, 30))
        # Seventh line
        self.pushButtonG1 = QPushButton(self.centralwidget)
        self.pushButtonG1.setGeometry(QRect(10, 210, 30, 30))
        self.pushButtonG2 = QPushButton(self.centralwidget)
        self.pushButtonG2.setGeometry(QRect(40, 210, 30, 30))
        self.pushButtonG3 = QPushButton(self.centralwidget)
        self.pushButtonG3.setGeometry(QRect(70, 210, 30, 30))
        self.pushButtonG4 = QPushButton(self.centralwidget)
        self.pushButtonG4.setGeometry(QRect(100, 210, 30, 30))
        self.pushButtonG5 = QPushButton(self.centralwidget)
        self.pushButtonG5.setGeometry(QRect(130, 210, 30, 30))
        self.pushButtonG6 = QPushButton(self.centralwidget)
        self.pushButtonG6.setGeometry(QRect(160, 210, 30, 30))
        self.pushButtonG7 = QPushButton(self.centralwidget)
        self.pushButtonG7.setGeometry(QRect(190, 210, 30, 30))
        self.pushButtonG8 = QPushButton(self.centralwidget)
        self.pushButtonG8.setGeometry(QRect(220, 210, 30, 30))
        self.pushButtonG9 = QPushButton(self.centralwidget)
        self.pushButtonG9.setGeometry(QRect(250, 210, 30, 30))
        self.pushButtonG10 = QPushButton(self.centralwidget)
        self.pushButtonG10.setGeometry(QRect(280, 210, 30, 30))
        self.pushButtonG11 = QPushButton(self.centralwidget)
        self.pushButtonG11.setGeometry(QRect(310, 210, 30, 30))
        self.pushButtonG12 = QPushButton(self.centralwidget)
        self.pushButtonG12.setGeometry(QRect(340, 210, 30, 30))
        self.pushButtonG13 = QPushButton(self.centralwidget)
        self.pushButtonG13.setGeometry(QRect(370, 210, 30, 30))
        self.pushButtonG14 = QPushButton(self.centralwidget)
        self.pushButtonG14.setGeometry(QRect(400, 210, 30, 30))
        self.pushButtonG15 = QPushButton(self.centralwidget)
        self.pushButtonG15.setGeometry(QRect(430, 210, 30, 30))
        # Eighth line
        self.pushButtonH1 = QPushButton(self.centralwidget)
        self.pushButtonH1.setGeometry(QRect(10, 240, 30, 30))
        self.pushButtonH2 = QPushButton(self.centralwidget)
        self.pushButtonH2.setGeometry(QRect(40, 240, 30, 30))
        self.pushButtonH3 = QPushButton(self.centralwidget)
        self.pushButtonH3.setGeometry(QRect(70, 240, 30, 30))
        self.pushButtonH4 = QPushButton(self.centralwidget)
        self.pushButtonH4.setGeometry(QRect(100, 240, 30, 30))
        self.pushButtonH5 = QPushButton(self.centralwidget)
        self.pushButtonH5.setGeometry(QRect(130, 240, 30, 30))
        self.pushButtonH6 = QPushButton(self.centralwidget)
        self.pushButtonH6.setGeometry(QRect(160, 240, 30, 30))
        self.pushButtonH7 = QPushButton(self.centralwidget)
        self.pushButtonH7.setGeometry(QRect(190, 240, 30, 30))
        self.pushButtonH8 = QPushButton(self.centralwidget)
        self.pushButtonH8.setGeometry(QRect(220, 240, 30, 30))
        self.pushButtonH9 = QPushButton(self.centralwidget)
        self.pushButtonH9.setGeometry(QRect(250, 240, 30, 30))
        self.pushButtonH10 = QPushButton(self.centralwidget)
        self.pushButtonH10.setGeometry(QRect(280, 240, 30, 30))
        self.pushButtonH11 = QPushButton(self.centralwidget)
        self.pushButtonH11.setGeometry(QRect(310, 240, 30, 30))
        self.pushButtonH12 = QPushButton(self.centralwidget)
        self.pushButtonH12.setGeometry(QRect(340, 240, 30, 30))
        self.pushButtonH13 = QPushButton(self.centralwidget)
        self.pushButtonH13.setGeometry(QRect(370, 240, 30, 30))
        self.pushButtonH14 = QPushButton(self.centralwidget)
        self.pushButtonH14.setGeometry(QRect(400, 240, 30, 30))
        self.pushButtonH15 = QPushButton(self.centralwidget)
        self.pushButtonH15.setGeometry(QRect(430, 240, 30, 30))
        # Nineth line
        self.pushButtonI1 = QPushButton(self.centralwidget)
        self.pushButtonI1.setGeometry(QRect(10, 270, 30, 30))
        self.pushButtonI2 = QPushButton(self.centralwidget)
        self.pushButtonI2.setGeometry(QRect(40, 270, 30, 30))
        self.pushButtonI3 = QPushButton(self.centralwidget)
        self.pushButtonI3.setGeometry(QRect(70, 270, 30, 30))
        self.pushButtonI4 = QPushButton(self.centralwidget)
        self.pushButtonI4.setGeometry(QRect(100, 270, 30, 30))
        self.pushButtonI5 = QPushButton(self.centralwidget)
        self.pushButtonI5.setGeometry(QRect(130, 270, 30, 30))
        self.pushButtonI6 = QPushButton(self.centralwidget)
        self.pushButtonI6.setGeometry(QRect(160, 270, 30, 30))
        self.pushButtonI7 = QPushButton(self.centralwidget)
        self.pushButtonI7.setGeometry(QRect(190, 270, 30, 30))
        self.pushButtonI8 = QPushButton(self.centralwidget)
        self.pushButtonI8.setGeometry(QRect(220, 270, 30, 30))
        self.pushButtonI9 = QPushButton(self.centralwidget)
        self.pushButtonI9.setGeometry(QRect(250, 270, 30, 30))
        self.pushButtonI10 = QPushButton(self.centralwidget)
        self.pushButtonI10.setGeometry(QRect(280, 270, 30, 30))
        self.pushButtonI11 = QPushButton(self.centralwidget)
        self.pushButtonI11.setGeometry(QRect(310, 270, 30, 30))
        self.pushButtonI12 = QPushButton(self.centralwidget)
        self.pushButtonI12.setGeometry(QRect(340, 270, 30, 30))
        self.pushButtonI13 = QPushButton(self.centralwidget)
        self.pushButtonI13.setGeometry(QRect(370, 270, 30, 30))
        self.pushButtonI14 = QPushButton(self.centralwidget)
        self.pushButtonI14.setGeometry(QRect(400, 270, 30, 30))
        self.pushButtonI15 = QPushButton(self.centralwidget)
        self.pushButtonI15.setGeometry(QRect(430, 270, 30, 30))
        # Tenth line
        self.pushButtonJ1 = QPushButton(self.centralwidget)
        self.pushButtonJ1.setGeometry(QRect(10, 300, 30, 30))
        self.pushButtonJ2 = QPushButton(self.centralwidget)
        self.pushButtonJ2.setGeometry(QRect(40, 300, 30, 30))
        self.pushButtonJ3 = QPushButton(self.centralwidget)
        self.pushButtonJ3.setGeometry(QRect(70, 300, 30, 30))
        self.pushButtonJ4 = QPushButton(self.centralwidget)
        self.pushButtonJ4.setGeometry(QRect(100, 300, 30, 30))
        self.pushButtonJ5 = QPushButton(self.centralwidget)
        self.pushButtonJ5.setGeometry(QRect(130, 300, 30, 30))
        self.pushButtonJ6 = QPushButton(self.centralwidget)
        self.pushButtonJ6.setGeometry(QRect(160, 300, 30, 30))
        self.pushButtonJ7 = QPushButton(self.centralwidget)
        self.pushButtonJ7.setGeometry(QRect(190, 300, 30, 30))
        self.pushButtonJ8 = QPushButton(self.centralwidget)
        self.pushButtonJ8.setGeometry(QRect(220, 300, 30, 30))
        self.pushButtonJ9 = QPushButton(self.centralwidget)
        self.pushButtonJ9.setGeometry(QRect(250, 300, 30, 30))
        self.pushButtonJ10 = QPushButton(self.centralwidget)
        self.pushButtonJ10.setGeometry(QRect(280, 300, 30, 30))
        self.pushButtonJ11 = QPushButton(self.centralwidget)
        self.pushButtonJ11.setGeometry(QRect(310, 300, 30, 30))
        self.pushButtonJ12 = QPushButton(self.centralwidget)
        self.pushButtonJ12.setGeometry(QRect(340, 300, 30, 30))
        self.pushButtonJ13 = QPushButton(self.centralwidget)
        self.pushButtonJ13.setGeometry(QRect(370, 300, 30, 30))
        self.pushButtonJ14 = QPushButton(self.centralwidget)
        self.pushButtonJ14.setGeometry(QRect(400, 300, 30, 30))
        self.pushButtonJ15 = QPushButton(self.centralwidget)
        self.pushButtonJ15.setGeometry(QRect(430, 300, 30, 30))
        # Eleventh line
        self.pushButtonK1 = QPushButton(self.centralwidget)
        self.pushButtonK1.setGeometry(QRect(10, 330, 30, 30))
        self.pushButtonK2 = QPushButton(self.centralwidget)
        self.pushButtonK2.setGeometry(QRect(40, 330, 30, 30))
        self.pushButtonK3 = QPushButton(self.centralwidget)
        self.pushButtonK3.setGeometry(QRect(70, 330, 30, 30))
        self.pushButtonK4 = QPushButton(self.centralwidget)
        self.pushButtonK4.setGeometry(QRect(100, 330, 30, 30))
        self.pushButtonK5 = QPushButton(self.centralwidget)
        self.pushButtonK5.setGeometry(QRect(130, 330, 30, 30))
        self.pushButtonK6 = QPushButton(self.centralwidget)
        self.pushButtonK6.setGeometry(QRect(160, 330, 30, 30))
        self.pushButtonK7 = QPushButton(self.centralwidget)
        self.pushButtonK7.setGeometry(QRect(190, 330, 30, 30))
        self.pushButtonK8 = QPushButton(self.centralwidget)
        self.pushButtonK8.setGeometry(QRect(220, 330, 30, 30))
        self.pushButtonK9 = QPushButton(self.centralwidget)
        self.pushButtonK9.setGeometry(QRect(250, 330, 30, 30))
        self.pushButtonK10 = QPushButton(self.centralwidget)
        self.pushButtonK10.setGeometry(QRect(280, 330, 30, 30))
        self.pushButtonK11 = QPushButton(self.centralwidget)
        self.pushButtonK11.setGeometry(QRect(310, 330, 30, 30))
        self.pushButtonK12 = QPushButton(self.centralwidget)
        self.pushButtonK12.setGeometry(QRect(340, 330, 30, 30))
        self.pushButtonK13 = QPushButton(self.centralwidget)
        self.pushButtonK13.setGeometry(QRect(370, 330, 30, 30))
        self.pushButtonK14 = QPushButton(self.centralwidget)
        self.pushButtonK14.setGeometry(QRect(400, 330, 30, 30))
        self.pushButtonK15 = QPushButton(self.centralwidget)
        self.pushButtonK15.setGeometry(QRect(430, 330, 30, 30))
        # Twelveth line
        self.pushButtonL1 = QPushButton(self.centralwidget)
        self.pushButtonL1.setGeometry(QRect(10, 360, 30, 30))
        self.pushButtonL2 = QPushButton(self.centralwidget)
        self.pushButtonL2.setGeometry(QRect(40, 360, 30, 30))
        self.pushButtonL3 = QPushButton(self.centralwidget)
        self.pushButtonL3.setGeometry(QRect(70, 360, 30, 30))
        self.pushButtonL4 = QPushButton(self.centralwidget)
        self.pushButtonL4.setGeometry(QRect(100, 360, 30, 30))
        self.pushButtonL5 = QPushButton(self.centralwidget)
        self.pushButtonL5.setGeometry(QRect(130, 360, 30, 30))
        self.pushButtonL6 = QPushButton(self.centralwidget)
        self.pushButtonL6.setGeometry(QRect(160, 360, 30, 30))
        self.pushButtonL7 = QPushButton(self.centralwidget)
        self.pushButtonL7.setGeometry(QRect(190, 360, 30, 30))
        self.pushButtonL8 = QPushButton(self.centralwidget)
        self.pushButtonL8.setGeometry(QRect(220, 360, 30, 30))
        self.pushButtonL9 = QPushButton(self.centralwidget)
        self.pushButtonL9.setGeometry(QRect(250, 360, 30, 30))
        self.pushButtonL10 = QPushButton(self.centralwidget)
        self.pushButtonL10.setGeometry(QRect(280, 360, 30, 30))
        self.pushButtonL11 = QPushButton(self.centralwidget)
        self.pushButtonL11.setGeometry(QRect(310, 360, 30, 30))
        self.pushButtonL12 = QPushButton(self.centralwidget)
        self.pushButtonL12.setGeometry(QRect(340, 360, 30, 30))
        self.pushButtonL13 = QPushButton(self.centralwidget)
        self.pushButtonL13.setGeometry(QRect(370, 360, 30, 30))
        self.pushButtonL14 = QPushButton(self.centralwidget)
        self.pushButtonL14.setGeometry(QRect(400, 360, 30, 30))
        self.pushButtonL15 = QPushButton(self.centralwidget)
        self.pushButtonL15.setGeometry(QRect(430, 360, 30, 30))
        # Thirteenth line
        self.pushButtonM1 = QPushButton(self.centralwidget)
        self.pushButtonM1.setGeometry(QRect(10, 390, 30, 30))
        self.pushButtonM2 = QPushButton(self.centralwidget)
        self.pushButtonM2.setGeometry(QRect(40, 390, 30, 30))
        self.pushButtonM3 = QPushButton(self.centralwidget)
        self.pushButtonM3.setGeometry(QRect(70, 390, 30, 30))
        self.pushButtonM4 = QPushButton(self.centralwidget)
        self.pushButtonM4.setGeometry(QRect(100, 390, 30, 30))
        self.pushButtonM5 = QPushButton(self.centralwidget)
        self.pushButtonM5.setGeometry(QRect(130, 390, 30, 30))
        self.pushButtonM6 = QPushButton(self.centralwidget)
        self.pushButtonM6.setGeometry(QRect(160, 390, 30, 30))
        self.pushButtonM7 = QPushButton(self.centralwidget)
        self.pushButtonM7.setGeometry(QRect(190, 390, 30, 30))
        self.pushButtonM8 = QPushButton(self.centralwidget)
        self.pushButtonM8.setGeometry(QRect(220, 390, 30, 30))
        self.pushButtonM9 = QPushButton(self.centralwidget)
        self.pushButtonM9.setGeometry(QRect(250, 390, 30, 30))
        self.pushButtonM10 = QPushButton(self.centralwidget)
        self.pushButtonM10.setGeometry(QRect(280, 390, 30, 30))
        self.pushButtonM11 = QPushButton(self.centralwidget)
        self.pushButtonM11.setGeometry(QRect(310, 390, 30, 30))
        self.pushButtonM12 = QPushButton(self.centralwidget)
        self.pushButtonM12.setGeometry(QRect(340, 390, 30, 30))
        self.pushButtonM13 = QPushButton(self.centralwidget)
        self.pushButtonM13.setGeometry(QRect(370, 390, 30, 30))
        self.pushButtonM14 = QPushButton(self.centralwidget)
        self.pushButtonM14.setGeometry(QRect(400, 390, 30, 30))
        self.pushButtonM15 = QPushButton(self.centralwidget)
        self.pushButtonM15.setGeometry(QRect(430, 390, 30, 30))
        # Fourteenth line
        self.pushButtonN1 = QPushButton(self.centralwidget)
        self.pushButtonN1.setGeometry(QRect(10, 420, 30, 30))
        self.pushButtonN2 = QPushButton(self.centralwidget)
        self.pushButtonN2.setGeometry(QRect(40, 420, 30, 30))
        self.pushButtonN3 = QPushButton(self.centralwidget)
        self.pushButtonN3.setGeometry(QRect(70, 420, 30, 30))
        self.pushButtonN4 = QPushButton(self.centralwidget)
        self.pushButtonN4.setGeometry(QRect(100, 420, 30, 30))
        self.pushButtonN5 = QPushButton(self.centralwidget)
        self.pushButtonN5.setGeometry(QRect(130, 420, 30, 30))
        self.pushButtonN6 = QPushButton(self.centralwidget)
        self.pushButtonN6.setGeometry(QRect(160, 420, 30, 30))
        self.pushButtonN7 = QPushButton(self.centralwidget)
        self.pushButtonN7.setGeometry(QRect(190, 420, 30, 30))
        self.pushButtonN8 = QPushButton(self.centralwidget)
        self.pushButtonN8.setGeometry(QRect(220, 420, 30, 30))
        self.pushButtonN9 = QPushButton(self.centralwidget)
        self.pushButtonN9.setGeometry(QRect(250, 420, 30, 30))
        self.pushButtonN10 = QPushButton(self.centralwidget)
        self.pushButtonN10.setGeometry(QRect(280, 420, 30, 30))
        self.pushButtonN11 = QPushButton(self.centralwidget)
        self.pushButtonN11.setGeometry(QRect(310, 420, 30, 30))
        self.pushButtonN12 = QPushButton(self.centralwidget)
        self.pushButtonN12.setGeometry(QRect(340, 420, 30, 30))
        self.pushButtonN13 = QPushButton(self.centralwidget)
        self.pushButtonN13.setGeometry(QRect(370, 420, 30, 30))
        self.pushButtonN14 = QPushButton(self.centralwidget)
        self.pushButtonN14.setGeometry(QRect(400, 420, 30, 30))
        self.pushButtonN15 = QPushButton(self.centralwidget)
        self.pushButtonN15.setGeometry(QRect(430, 420, 30, 30))
        # Fiveteenth line
        self.pushButtonO1 = QPushButton(self.centralwidget)
        self.pushButtonO1.setGeometry(QRect(10, 450, 30, 30))
        self.pushButtonO2 = QPushButton(self.centralwidget)
        self.pushButtonO2.setGeometry(QRect(40, 450, 30, 30))
        self.pushButtonO3 = QPushButton(self.centralwidget)
        self.pushButtonO3.setGeometry(QRect(70, 450, 30, 30))
        self.pushButtonO4 = QPushButton(self.centralwidget)
        self.pushButtonO4.setGeometry(QRect(100, 450, 30, 30))
        self.pushButtonO5 = QPushButton(self.centralwidget)
        self.pushButtonO5.setGeometry(QRect(130, 450, 30, 30))
        self.pushButtonO6 = QPushButton(self.centralwidget)
        self.pushButtonO6.setGeometry(QRect(160, 450, 30, 30))
        self.pushButtonO7 = QPushButton(self.centralwidget)
        self.pushButtonO7.setGeometry(QRect(190, 450, 30, 30))
        self.pushButtonO8 = QPushButton(self.centralwidget)
        self.pushButtonO8.setGeometry(QRect(220, 450, 30, 30))
        self.pushButtonO9 = QPushButton(self.centralwidget)
        self.pushButtonO9.setGeometry(QRect(250, 450, 30, 30))
        self.pushButtonO10 = QPushButton(self.centralwidget)
        self.pushButtonO10.setGeometry(QRect(280, 450, 30, 30))
        self.pushButtonO11 = QPushButton(self.centralwidget)
        self.pushButtonO11.setGeometry(QRect(310, 450, 30, 30))
        self.pushButtonO12 = QPushButton(self.centralwidget)
        self.pushButtonO12.setGeometry(QRect(340, 450, 30, 30))
        self.pushButtonO13 = QPushButton(self.centralwidget)
        self.pushButtonO13.setGeometry(QRect(370, 450, 30, 30))
        self.pushButtonO14 = QPushButton(self.centralwidget)
        self.pushButtonO14.setGeometry(QRect(400, 450, 30, 30))
        self.pushButtonO15 = QPushButton(self.centralwidget)
        self.pushButtonO15.setGeometry(QRect(430, 450, 30, 30))

        self.pushButtonFlag = ButtonFlag(self.centralwidget, QRect(460, 450, 30, 30))

        MainWindow.setCentralWidget(self.centralwidget)
        self.create_board()
        self.icons = Icon()
        for i in range(Ui_MainWindow.LENGTH_AXIS_Y):
            for j in range(Ui_MainWindow.LENGTH_AXIS_X):
                self.board[i][j].value = '0'
                """
        for i in range(Ui_MainWindow.LENGTH_AXIS_Y):
            for j in range(Ui_MainWindow.LENGTH_AXIS_X):
                self.board[i][j].value = '0'
        self.board[0][0].clicked.connect(self.click_pushButtonA1)
        self.pushButtonA2.clicked.connect(self.click_pushButtonA2)
        self.pushButtonA3.clicked.connect(self.click_pushButtonA3)
        self.pushButtonB1.clicked.connect(self.click_pushButtonB1)
        self.pushButtonB2.clicked.connect(self.click_pushButtonB2)
        self.pushButtonB3.clicked.connect(self.click_pushButtonB3)
        self.pushButtonC1.clicked.connect(self.click_pushButtonC1)
        self.pushButtonC2.clicked.connect(self.click_pushButtonC2)
        self.pushButtonC3.clicked.connect(self.click_pushButtonC3)"""


        self.bombs_position_raffle()
        print('pos as bombas')
        self.define_other_fields()

        self.function_click_buttons = \
            [[self.click_pushButtonA1, self.click_pushButtonA2, self.click_pushButtonA3, self.click_pushButtonA4,
              self.click_pushButtonA5, self.click_pushButtonA6, self.click_pushButtonA7, self.click_pushButtonA8,
              self.click_pushButtonA9, self.click_pushButtonA10, self.click_pushButtonA11, self.click_pushButtonA12,
              self.click_pushButtonA13, self.click_pushButtonA14, self.click_pushButtonA15],
             [self.click_pushButtonB1, self.click_pushButtonB2, self.click_pushButtonB3, self.click_pushButtonB4,
              self.click_pushButtonB5, self.click_pushButtonB6, self.click_pushButtonB7, self.click_pushButtonB8,
              self.click_pushButtonB9, self.click_pushButtonB10, self.click_pushButtonB11, self.click_pushButtonB12,
              self.click_pushButtonB13, self.click_pushButtonB14, self.click_pushButtonB15],
             [self.click_pushButtonC1, self.click_pushButtonC2, self.click_pushButtonC3, self.click_pushButtonC4,
              self.click_pushButtonC5, self.click_pushButtonC6, self.click_pushButtonC7, self.click_pushButtonC8,
              self.click_pushButtonC9, self.click_pushButtonC10, self.click_pushButtonC11, self.click_pushButtonC12,
              self.click_pushButtonC13, self.click_pushButtonC14, self.click_pushButtonC15],
             [self.click_pushButtonD1, self.click_pushButtonD2, self.click_pushButtonD3, self.click_pushButtonD4,
              self.click_pushButtonD5, self.click_pushButtonD6, self.click_pushButtonD7, self.click_pushButtonD8,
              self.click_pushButtonD9, self.click_pushButtonD10, self.click_pushButtonD11, self.click_pushButtonD12,
              self.click_pushButtonD13, self.click_pushButtonD14, self.click_pushButtonD15],
             [self.click_pushButtonE1, self.click_pushButtonE2, self.click_pushButtonE3, self.click_pushButtonE4,
              self.click_pushButtonE5, self.click_pushButtonE6, self.click_pushButtonE7, self.click_pushButtonE8,
              self.click_pushButtonE9, self.click_pushButtonE10, self.click_pushButtonE11, self.click_pushButtonE12,
              self.click_pushButtonE13, self.click_pushButtonE14, self.click_pushButtonE15],
             [self.click_pushButtonF1, self.click_pushButtonF2, self.click_pushButtonF3, self.click_pushButtonF4,
              self.click_pushButtonF5, self.click_pushButtonF6, self.click_pushButtonF7, self.click_pushButtonF8,
              self.click_pushButtonF9, self.click_pushButtonF10, self.click_pushButtonF11, self.click_pushButtonF12,
              self.click_pushButtonF13, self.click_pushButtonF14, self.click_pushButtonF15],
             [self.click_pushButtonG1, self.click_pushButtonG2, self.click_pushButtonG3, self.click_pushButtonG4,
              self.click_pushButtonG5, self.click_pushButtonG6, self.click_pushButtonG7, self.click_pushButtonG8,
              self.click_pushButtonG9, self.click_pushButtonG10, self.click_pushButtonG11, self.click_pushButtonG12,
              self.click_pushButtonG13, self.click_pushButtonG14, self.click_pushButtonG15],
             [self.click_pushButtonH1, self.click_pushButtonH2, self.click_pushButtonH3, self.click_pushButtonH4,
              self.click_pushButtonH5, self.click_pushButtonH6, self.click_pushButtonH7, self.click_pushButtonH8,
              self.click_pushButtonH9, self.click_pushButtonH10, self.click_pushButtonH11, self.click_pushButtonH12,
              self.click_pushButtonH13, self.click_pushButtonH14, self.click_pushButtonH15],
             [self.click_pushButtonI1, self.click_pushButtonI2, self.click_pushButtonI3, self.click_pushButtonI4,
              self.click_pushButtonI5, self.click_pushButtonI6, self.click_pushButtonI7, self.click_pushButtonI8,
              self.click_pushButtonI9, self.click_pushButtonI10, self.click_pushButtonI11, self.click_pushButtonI12,
              self.click_pushButtonI13, self.click_pushButtonI14, self.click_pushButtonI15],
             [self.click_pushButtonJ1, self.click_pushButtonJ2, self.click_pushButtonJ3, self.click_pushButtonJ4,
              self.click_pushButtonJ5, self.click_pushButtonJ6, self.click_pushButtonJ7, self.click_pushButtonJ8,
              self.click_pushButtonJ9, self.click_pushButtonJ10, self.click_pushButtonJ11, self.click_pushButtonJ12,
              self.click_pushButtonJ13, self.click_pushButtonJ14, self.click_pushButtonJ15],
             [self.click_pushButtonK1, self.click_pushButtonK2, self.click_pushButtonK3, self.click_pushButtonK4,
              self.click_pushButtonK5, self.click_pushButtonK6, self.click_pushButtonK7, self.click_pushButtonK8,
              self.click_pushButtonK9, self.click_pushButtonK10, self.click_pushButtonK11, self.click_pushButtonK12,
              self.click_pushButtonK13, self.click_pushButtonK14, self.click_pushButtonK15],
             [self.click_pushButtonL1, self.click_pushButtonL2, self.click_pushButtonL3, self.click_pushButtonL4,
              self.click_pushButtonL5, self.click_pushButtonL6, self.click_pushButtonL7, self.click_pushButtonL8,
              self.click_pushButtonL9, self.click_pushButtonL10, self.click_pushButtonL11, self.click_pushButtonL12,
              self.click_pushButtonL13, self.click_pushButtonL14, self.click_pushButtonL15],
             [self.click_pushButtonM1, self.click_pushButtonM2, self.click_pushButtonM3, self.click_pushButtonM4,
              self.click_pushButtonM5, self.click_pushButtonM6, self.click_pushButtonM7, self.click_pushButtonM8,
              self.click_pushButtonM9, self.click_pushButtonM10, self.click_pushButtonM11, self.click_pushButtonM12,
              self.click_pushButtonM13, self.click_pushButtonM14, self.click_pushButtonM15],
             [self.click_pushButtonN1, self.click_pushButtonN2, self.click_pushButtonN3, self.click_pushButtonN4,
              self.click_pushButtonN5, self.click_pushButtonN6, self.click_pushButtonN7, self.click_pushButtonN8,
              self.click_pushButtonN9, self.click_pushButtonN10, self.click_pushButtonN11, self.click_pushButtonN12,
              self.click_pushButtonN13, self.click_pushButtonN14, self.click_pushButtonN15],
             [self.click_pushButtonO1, self.click_pushButtonO2, self.click_pushButtonO3, self.click_pushButtonO4,
              self.click_pushButtonO5, self.click_pushButtonO6, self.click_pushButtonO7, self.click_pushButtonO8,
              self.click_pushButtonO9, self.click_pushButtonO10, self.click_pushButtonO11, self.click_pushButtonO12,
              self.click_pushButtonO13, self.click_pushButtonO14, self.click_pushButtonO15]]

        for i in range(Ui_MainWindow.LENGTH_AXIS_Y):
            for j in range(Ui_MainWindow.LENGTH_AXIS_X):
                self.board[i][j].clicked.connect(self.function_click_buttons[i][j])

    def get_range_limits(self, x, y):
        x_min = 0 if x - 1 < 0 else x - 1
        x_max = Ui_MainWindow.LENGTH_AXIS_X if x + 2 > Ui_MainWindow.LENGTH_AXIS_X else x + 2
        y_min = 0 if y - 1 < 0 else y - 1
        y_max = Ui_MainWindow.LENGTH_AXIS_Y if y + 2 > Ui_MainWindow.LENGTH_AXIS_Y else y + 2
        return x_min, x_max, y_min, y_max

    def process_neighbour_buttons(self, x, y):
        x_min, x_max, y_min, y_max = self.get_range_limits(x, y)
        for i in range(x_min, x_max):
            for j in range(y_min, y_max):
                if self.board[j][i].isEnabled():
                    self.function_click_buttons[j][i]()

    def click_pushButtonA1(self):
        if self.abrir(0, 0) == '0':
            self.process_neighbour_buttons(0, 0)

    def click_pushButtonA2(self):
        if self.abrir(1, 0) == '0':
            self.process_neighbour_buttons(1, 0)

    def click_pushButtonA3(self):
        if self.abrir(2, 0) == '0':
            self.process_neighbour_buttons(2, 0)

    def click_pushButtonA4(self):
        if self.abrir(3, 0) == '0':
            self.process_neighbour_buttons(3, 0)

    def click_pushButtonA5(self):
        if self.abrir(4, 0) == '0':
            self.process_neighbour_buttons(4, 0)

    def click_pushButtonA6(self):
        if self.abrir(5, 0) == '0':
            self.process_neighbour_buttons(5, 0)

    def click_pushButtonA7(self):
        if self.abrir(6, 0) == '0':
            self.process_neighbour_buttons(6, 0)

    def click_pushButtonA8(self):
        if self.abrir(7, 0) == '0':
            self.process_neighbour_buttons(7, 0)

    def click_pushButtonA9(self):
        if self.abrir(8, 0) == '0':
            self.process_neighbour_buttons(8, 0)

    def click_pushButtonA10(self):
        if self.abrir(9, 0) == '0':
            self.process_neighbour_buttons(9, 0)

    def click_pushButtonA11(self):
        if self.abrir(10, 0) == '0':
            self.process_neighbour_buttons(10, 0)

    def click_pushButtonA12(self):
        if self.abrir(11, 0) == '0':
            self.process_neighbour_buttons(11, 0)

    def click_pushButtonA13(self):
        if self.abrir(12, 0) == '0':
            self.process_neighbour_buttons(12, 0)

    def click_pushButtonA14(self):
        if self.abrir(13, 0) == '0':
            self.process_neighbour_buttons(13, 0)

    def click_pushButtonA15(self):
        if self.abrir(14, 0) == '0':
            self.process_neighbour_buttons(14, 0)

    def click_pushButtonB1(self):
        if self.abrir(0, 1) == '0':
            self.process_neighbour_buttons(0, 1)

    def click_pushButtonB2(self):
        if self.abrir(1, 1) == '0':
            self.process_neighbour_buttons(1, 1)

    def click_pushButtonB3(self):
        if self.abrir(2, 1) == '0':
            self.process_neighbour_buttons(2, 1)

    def click_pushButtonB4(self):
        if self.abrir(3, 1) == '0':
            self.process_neighbour_buttons(3, 1)

    def click_pushButtonB5(self):
        if self.abrir(4, 1) == '0':
            self.process_neighbour_buttons(4, 1)

    def click_pushButtonB6(self):
        if self.abrir(5, 1) == '0':
            self.process_neighbour_buttons(5, 1)

    def click_pushButtonB7(self):
        if self.abrir(6, 1) == '0':
            self.process_neighbour_buttons(6, 1)

    def click_pushButtonB8(self):
        if self.abrir(7, 1) == '0':
            self.process_neighbour_buttons(7, 1)

    def click_pushButtonB9(self):
        if self.abrir(8, 1) == '0':
            self.process_neighbour_buttons(8, 1)

    def click_pushButtonB10(self):
        if self.abrir(9, 1) == '0':
            self.process_neighbour_buttons(9, 1)

    def click_pushButtonB11(self):
        if self.abrir(10, 1) == '0':
            self.process_neighbour_buttons(10, 1)

    def click_pushButtonB12(self):
        if self.abrir(11, 1) == '0':
            self.process_neighbour_buttons(11, 1)

    def click_pushButtonB13(self):
        if self.abrir(12, 1) == '0':
            self.process_neighbour_buttons(12, 1)

    def click_pushButtonB14(self):
        if self.abrir(13, 1) == '0':
            self.process_neighbour_buttons(13, 1)

    def click_pushButtonB15(self):
        if self.abrir(14, 1) == '0':
            self.process_neighbour_buttons(14, 1)

    def click_pushButtonC1(self):
        if self.abrir(0, 2) == '0':
            self.process_neighbour_buttons(0, 2)

    def click_pushButtonC2(self):
        if self.abrir(1, 2) == '0':
            self.process_neighbour_buttons(1, 2)

    def click_pushButtonC3(self):
        if self.abrir(2, 2) == '0':
            self.process_neighbour_buttons(2, 2)

    def click_pushButtonC4(self):
        if self.abrir(3, 2) == '0':
            self.process_neighbour_buttons(3, 2)

    def click_pushButtonC5(self):
        if self.abrir(4, 2) == '0':
            self.process_neighbour_buttons(4, 2)

    def click_pushButtonC6(self):
        if self.abrir(5, 2) == '0':
            self.process_neighbour_buttons(5, 2)

    def click_pushButtonC7(self):
        if self.abrir(6, 2) == '0':
            self.process_neighbour_buttons(6, 2)

    def click_pushButtonC8(self):
        if self.abrir(7, 2) == '0':
            self.process_neighbour_buttons(7, 2)

    def click_pushButtonC9(self):
        if self.abrir(8, 2) == '0':
            self.process_neighbour_buttons(8, 2)

    def click_pushButtonC10(self):
        if self.abrir(9, 2) == '0':
            self.process_neighbour_buttons(9, 2)

    def click_pushButtonC11(self):
        if self.abrir(10, 2) == '0':
            self.process_neighbour_buttons(10, 2)

    def click_pushButtonC12(self):
        if self.abrir(11, 2) == '0':
            self.process_neighbour_buttons(11, 2)

    def click_pushButtonC13(self):
        if self.abrir(12, 2) == '0':
            self.process_neighbour_buttons(12, 2)

    def click_pushButtonC14(self):
        if self.abrir(13, 2) == '0':
            self.process_neighbour_buttons(13, 2)

    def click_pushButtonC15(self):
        if self.abrir(14, 2) == '0':
            self.process_neighbour_buttons(14, 2)

    def click_pushButtonD1(self):
        if self.abrir(0, 3) == '0':
            self.process_neighbour_buttons(0, 3)

    def click_pushButtonD2(self):
        if self.abrir(1, 3) == '0':
            self.process_neighbour_buttons(1, 3)

    def click_pushButtonD3(self):
        if self.abrir(2, 3) == '0':
            self.process_neighbour_buttons(2, 3)

    def click_pushButtonD4(self):
        if self.abrir(3, 3) == '0':
            self.process_neighbour_buttons(3, 3)

    def click_pushButtonD5(self):
        if self.abrir(4, 3) == '0':
            self.process_neighbour_buttons(4, 3)

    def click_pushButtonD6(self):
        if self.abrir(5, 3) == '0':
            self.process_neighbour_buttons(5, 3)

    def click_pushButtonD7(self):
        if self.abrir(6, 3) == '0':
            self.process_neighbour_buttons(6, 3)

    def click_pushButtonD8(self):
        if self.abrir(7, 3) == '0':
            self.process_neighbour_buttons(7, 3)

    def click_pushButtonD9(self):
        if self.abrir(8, 3) == '0':
            self.process_neighbour_buttons(8, 3)

    def click_pushButtonD10(self):
        if self.abrir(9, 3) == '0':
            self.process_neighbour_buttons(9, 3)

    def click_pushButtonD11(self):
        if self.abrir(10, 3) == '0':
            self.process_neighbour_buttons(10, 3)

    def click_pushButtonD12(self):
        if self.abrir(11, 3) == '0':
            self.process_neighbour_buttons(11, 3)

    def click_pushButtonD13(self):
        if self.abrir(12, 3) == '0':
            self.process_neighbour_buttons(12, 3)

    def click_pushButtonD14(self):
        if self.abrir(13, 3) == '0':
            self.process_neighbour_buttons(13, 3)

    def click_pushButtonD15(self):
        if self.abrir(14, 3) == '0':
            self.process_neighbour_buttons(14, 3)

    def click_pushButtonE1(self):
        if self.abrir(0, 4) == '0':
            self.process_neighbour_buttons(0, 4)

    def click_pushButtonE2(self):
        if self.abrir(1, 4) == '0':
            self.process_neighbour_buttons(1, 4)

    def click_pushButtonE3(self):
        if self.abrir(2, 4) == '0':
            self.process_neighbour_buttons(2, 4)

    def click_pushButtonE4(self):
        if self.abrir(3, 4) == '0':
            self.process_neighbour_buttons(3, 4)

    def click_pushButtonE5(self):
        if self.abrir(4, 4) == '0':
            self.process_neighbour_buttons(4, 4)

    def click_pushButtonE6(self):
        if self.abrir(5, 4) == '0':
            self.process_neighbour_buttons(5, 4)

    def click_pushButtonE7(self):
        if self.abrir(6, 4) == '0':
            self.process_neighbour_buttons(6, 4)

    def click_pushButtonE8(self):
        if self.abrir(7, 4) == '0':
            self.process_neighbour_buttons(7, 4)

    def click_pushButtonE9(self):
        if self.abrir(8, 4) == '0':
            self.process_neighbour_buttons(8, 4)

    def click_pushButtonE10(self):
        if self.abrir(9, 4) == '0':
            self.process_neighbour_buttons(9, 4)

    def click_pushButtonE11(self):
        if self.abrir(10, 4) == '0':
            self.process_neighbour_buttons(10, 4)

    def click_pushButtonE12(self):
        if self.abrir(11, 4) == '0':
            self.process_neighbour_buttons(11, 4)

    def click_pushButtonE13(self):
        if self.abrir(12, 4) == '0':
            self.process_neighbour_buttons(12, 4)

    def click_pushButtonE14(self):
        if self.abrir(13, 4) == '0':
            self.process_neighbour_buttons(13, 4)

    def click_pushButtonE15(self):
        if self.abrir(14, 4) == '0':
            self.process_neighbour_buttons(14, 4)

    def click_pushButtonF1(self):
        if self.abrir(0, 5) == '0':
            self.process_neighbour_buttons(0, 5)

    def click_pushButtonF2(self):
        if self.abrir(1, 5) == '0':
            self.process_neighbour_buttons(1, 5)

    def click_pushButtonF3(self):
        if self.abrir(2, 5) == '0':
            self.process_neighbour_buttons(2, 5)

    def click_pushButtonF4(self):
        if self.abrir(3, 5) == '0':
            self.process_neighbour_buttons(3, 5)

    def click_pushButtonF5(self):
        if self.abrir(4, 5) == '0':
            self.process_neighbour_buttons(4, 5)

    def click_pushButtonF6(self):
        if self.abrir(5, 5) == '0':
            self.process_neighbour_buttons(5, 5)

    def click_pushButtonF7(self):
        if self.abrir(6, 5) == '0':
            self.process_neighbour_buttons(6, 5)

    def click_pushButtonF8(self):
        if self.abrir(7, 5) == '0':
            self.process_neighbour_buttons(7, 5)

    def click_pushButtonF9(self):
        if self.abrir(8, 5) == '0':
            self.process_neighbour_buttons(8, 5)

    def click_pushButtonF10(self):
        if self.abrir(9, 5) == '0':
            self.process_neighbour_buttons(9, 5)

    def click_pushButtonF11(self):
        if self.abrir(10, 5) == '0':
            self.process_neighbour_buttons(10, 5)

    def click_pushButtonF12(self):
        if self.abrir(11, 5) == '0':
            self.process_neighbour_buttons(11, 5)

    def click_pushButtonF13(self):
        if self.abrir(12, 5) == '0':
            self.process_neighbour_buttons(12, 5)

    def click_pushButtonF14(self):
        if self.abrir(13, 5) == '0':
            self.process_neighbour_buttons(13, 5)

    def click_pushButtonF15(self):
        if self.abrir(14, 5) == '0':
            self.process_neighbour_buttons(14, 5)

    def click_pushButtonG1(self):
        if self.abrir(0, 6) == '0':
            self.process_neighbour_buttons(0, 6)

    def click_pushButtonG2(self):
        if self.abrir(1, 6) == '0':
            self.process_neighbour_buttons(1, 6)

    def click_pushButtonG3(self):
        if self.abrir(2, 6) == '0':
            self.process_neighbour_buttons(2, 6)

    def click_pushButtonG4(self):
        if self.abrir(3, 6) == '0':
            self.process_neighbour_buttons(3, 6)

    def click_pushButtonG5(self):
        if self.abrir(4, 6) == '0':
            self.process_neighbour_buttons(4, 6)

    def click_pushButtonG6(self):
        if self.abrir(5, 6) == '0':
            self.process_neighbour_buttons(5, 6)

    def click_pushButtonG7(self):
        if self.abrir(6, 6) == '0':
            self.process_neighbour_buttons(6, 6)

    def click_pushButtonG8(self):
        if self.abrir(7, 6) == '0':
            self.process_neighbour_buttons(7, 6)

    def click_pushButtonG9(self):
        if self.abrir(8, 6) == '0':
            self.process_neighbour_buttons(8, 6)

    def click_pushButtonG10(self):
        if self.abrir(9, 6) == '0':
            self.process_neighbour_buttons(9, 6)

    def click_pushButtonG11(self):
        if self.abrir(10, 6) == '0':
            self.process_neighbour_buttons(10, 6)

    def click_pushButtonG12(self):
        if self.abrir(11, 6) == '0':
            self.process_neighbour_buttons(11, 6)

    def click_pushButtonG13(self):
        if self.abrir(12, 6) == '0':
            self.process_neighbour_buttons(12, 6)

    def click_pushButtonG14(self):
        if self.abrir(13, 6) == '0':
            self.process_neighbour_buttons(13, 6)

    def click_pushButtonG15(self):
        if self.abrir(14, 6) == '0':
            self.process_neighbour_buttons(14, 6)

    def click_pushButtonH1(self):
        if self.abrir(0, 7) == '0':
            self.process_neighbour_buttons(0, 7)

    def click_pushButtonH2(self):
        if self.abrir(1, 7) == '0':
            self.process_neighbour_buttons(1, 7)

    def click_pushButtonH3(self):
        if self.abrir(2, 7) == '0':
            self.process_neighbour_buttons(2, 7)

    def click_pushButtonH4(self):
        if self.abrir(3, 7) == '0':
            self.process_neighbour_buttons(3, 7)

    def click_pushButtonH5(self):
        if self.abrir(4, 7) == '0':
            self.process_neighbour_buttons(4, 7)

    def click_pushButtonH6(self):
        if self.abrir(5, 7) == '0':
            self.process_neighbour_buttons(5, 7)

    def click_pushButtonH7(self):
        if self.abrir(6, 7) == '0':
            self.process_neighbour_buttons(6, 7)

    def click_pushButtonH8(self):
        if self.abrir(7, 7) == '0':
            self.process_neighbour_buttons(7, 7)

    def click_pushButtonH9(self):
        if self.abrir(8, 7) == '0':
            self.process_neighbour_buttons(8, 7)

    def click_pushButtonH10(self):
        if self.abrir(9, 7) == '0':
            self.process_neighbour_buttons(9, 7)

    def click_pushButtonH11(self):
        if self.abrir(10, 7) == '0':
            self.process_neighbour_buttons(10, 7)

    def click_pushButtonH12(self):
        if self.abrir(11, 7) == '0':
            self.process_neighbour_buttons(11, 7)

    def click_pushButtonH13(self):
        if self.abrir(12, 7) == '0':
            self.process_neighbour_buttons(12, 7)

    def click_pushButtonH14(self):
        if self.abrir(13, 7) == '0':
            self.process_neighbour_buttons(13, 7)

    def click_pushButtonH15(self):
        if self.abrir(14, 7) == '0':
            self.process_neighbour_buttons(14, 7)

    def click_pushButtonI1(self):
        if self.abrir(0, 8) == '0':
            self.process_neighbour_buttons(0, 8)

    def click_pushButtonI2(self):
        if self.abrir(1, 8) == '0':
            self.process_neighbour_buttons(1, 8)

    def click_pushButtonI3(self):
        if self.abrir(2, 8) == '0':
            self.process_neighbour_buttons(2, 8)

    def click_pushButtonI4(self):
        if self.abrir(3, 8) == '0':
            self.process_neighbour_buttons(3, 8)

    def click_pushButtonI5(self):
        if self.abrir(4, 8) == '0':
            self.process_neighbour_buttons(4, 8)

    def click_pushButtonI6(self):
        if self.abrir(5, 8) == '0':
            self.process_neighbour_buttons(5, 8)

    def click_pushButtonI7(self):
        if self.abrir(6, 8) == '0':
            self.process_neighbour_buttons(6, 8)

    def click_pushButtonI8(self):
        if self.abrir(7, 8) == '0':
            self.process_neighbour_buttons(7, 8)

    def click_pushButtonI9(self):
        if self.abrir(8, 8) == '0':
            self.process_neighbour_buttons(8, 8)

    def click_pushButtonI10(self):
        if self.abrir(9, 8) == '0':
            self.process_neighbour_buttons(9, 8)

    def click_pushButtonI11(self):
        if self.abrir(10, 8) == '0':
            self.process_neighbour_buttons(10, 8)

    def click_pushButtonI12(self):
        if self.abrir(11, 8) == '0':
            self.process_neighbour_buttons(11, 8)

    def click_pushButtonI13(self):
        if self.abrir(12, 8) == '0':
            self.process_neighbour_buttons(12, 8)

    def click_pushButtonI14(self):
        if self.abrir(13, 8) == '0':
            self.process_neighbour_buttons(13, 8)

    def click_pushButtonI15(self):
        if self.abrir(14, 8) == '0':
            self.process_neighbour_buttons(14, 8)

    def click_pushButtonJ1(self):
        if self.abrir(0, 9) == '0':
            self.process_neighbour_buttons(0, 9)

    def click_pushButtonJ2(self):
        if self.abrir(1, 9) == '0':
            self.process_neighbour_buttons(1, 9)

    def click_pushButtonJ3(self):
        if self.abrir(2, 9) == '0':
            self.process_neighbour_buttons(2, 9)

    def click_pushButtonJ4(self):
        if self.abrir(3, 9) == '0':
            self.process_neighbour_buttons(3, 9)

    def click_pushButtonJ5(self):
        if self.abrir(4, 9) == '0':
            self.process_neighbour_buttons(4, 9)

    def click_pushButtonJ6(self):
        if self.abrir(5, 9) == '0':
            self.process_neighbour_buttons(5, 9)

    def click_pushButtonJ7(self):
        if self.abrir(6, 9) == '0':
            self.process_neighbour_buttons(6, 9)

    def click_pushButtonJ8(self):
        if self.abrir(7, 9) == '0':
            self.process_neighbour_buttons(7, 9)

    def click_pushButtonJ9(self):
        if self.abrir(8, 9) == '0':
            self.process_neighbour_buttons(8, 9)

    def click_pushButtonJ10(self):
        if self.abrir(9, 9) == '0':
            self.process_neighbour_buttons(9, 9)

    def click_pushButtonJ11(self):
        if self.abrir(10, 9) == '0':
            self.process_neighbour_buttons(10, 9)

    def click_pushButtonJ12(self):
        if self.abrir(11, 9) == '0':
            self.process_neighbour_buttons(11, 9)

    def click_pushButtonJ13(self):
        if self.abrir(12, 9) == '0':
            self.process_neighbour_buttons(12, 9)

    def click_pushButtonJ14(self):
        if self.abrir(13, 9) == '0':
            self.process_neighbour_buttons(13, 9)

    def click_pushButtonJ15(self):
        if self.abrir(14, 9) == '0':
            self.process_neighbour_buttons(14, 9)

    def click_pushButtonK1(self):
        if self.abrir(0, 10) == '0':
            self.process_neighbour_buttons(0, 10)

    def click_pushButtonK2(self):
        if self.abrir(1, 10) == '0':
            self.process_neighbour_buttons(1, 10)

    def click_pushButtonK3(self):
        if self.abrir(2, 10) == '0':
            self.process_neighbour_buttons(2, 10)

    def click_pushButtonK4(self):
        if self.abrir(3, 10) == '0':
            self.process_neighbour_buttons(3, 10)

    def click_pushButtonK5(self):
        if self.abrir(4, 10) == '0':
            self.process_neighbour_buttons(4, 10)

    def click_pushButtonK6(self):
        if self.abrir(5, 10) == '0':
            self.process_neighbour_buttons(5, 10)

    def click_pushButtonK7(self):
        if self.abrir(6, 10) == '0':
            self.process_neighbour_buttons(6, 10)

    def click_pushButtonK8(self):
        if self.abrir(7, 10) == '0':
            self.process_neighbour_buttons(7, 10)

    def click_pushButtonK9(self):
        if self.abrir(8, 10) == '0':
            self.process_neighbour_buttons(8, 10)

    def click_pushButtonK10(self):
        if self.abrir(9, 10) == '0':
            self.process_neighbour_buttons(9, 10)

    def click_pushButtonK11(self):
        if self.abrir(10, 10) == '0':
            self.process_neighbour_buttons(10, 10)

    def click_pushButtonK12(self):
        if self.abrir(11, 10) == '0':
            self.process_neighbour_buttons(11, 10)

    def click_pushButtonK13(self):
        if self.abrir(12, 10) == '0':
            self.process_neighbour_buttons(12, 10)

    def click_pushButtonK14(self):
        if self.abrir(13, 10) == '0':
            self.process_neighbour_buttons(13, 10)

    def click_pushButtonK15(self):
        if self.abrir(14, 10) == '0':
            self.process_neighbour_buttons(14, 10)

    def click_pushButtonL1(self):
        if self.abrir(0, 11) == '0':
            self.process_neighbour_buttons(0, 11)

    def click_pushButtonL2(self):
        if self.abrir(1, 11) == '0':
            self.process_neighbour_buttons(1, 11)

    def click_pushButtonL3(self):
        if self.abrir(2, 11) == '0':
            self.process_neighbour_buttons(2, 11)

    def click_pushButtonL4(self):
        if self.abrir(3, 11) == '0':
            self.process_neighbour_buttons(3, 11)

    def click_pushButtonL5(self):
        if self.abrir(4, 11) == '0':
            self.process_neighbour_buttons(4, 11)

    def click_pushButtonL6(self):
        if self.abrir(5, 11) == '0':
            self.process_neighbour_buttons(5, 11)

    def click_pushButtonL7(self):
        if self.abrir(6, 11) == '0':
            self.process_neighbour_buttons(6, 11)

    def click_pushButtonL8(self):
        if self.abrir(7, 11) == '0':
            self.process_neighbour_buttons(7, 11)

    def click_pushButtonL9(self):
        if self.abrir(8, 11) == '0':
            self.process_neighbour_buttons(8, 11)

    def click_pushButtonL10(self):
        if self.abrir(9, 11) == '0':
            self.process_neighbour_buttons(9, 11)

    def click_pushButtonL11(self):
        if self.abrir(10, 11) == '0':
            self.process_neighbour_buttons(10, 11)

    def click_pushButtonL12(self):
        if self.abrir(11, 11) == '0':
            self.process_neighbour_buttons(11, 11)

    def click_pushButtonL13(self):
        if self.abrir(12, 11) == '0':
            self.process_neighbour_buttons(12, 11)

    def click_pushButtonL14(self):
        if self.abrir(13, 11) == '0':
            self.process_neighbour_buttons(13, 11)

    def click_pushButtonL15(self):
        if self.abrir(14, 11) == '0':
            self.process_neighbour_buttons(14, 11)

    def click_pushButtonM1(self):
        if self.abrir(0, 12) == '0':
            self.process_neighbour_buttons(0, 12)

    def click_pushButtonM2(self):
        if self.abrir(1, 12) == '0':
            self.process_neighbour_buttons(1, 12)

    def click_pushButtonM3(self):
        if self.abrir(2, 12) == '0':
            self.process_neighbour_buttons(2, 12)

    def click_pushButtonM4(self):
        if self.abrir(3, 12) == '0':
            self.process_neighbour_buttons(3, 12)

    def click_pushButtonM5(self):
        if self.abrir(4, 12) == '0':
            self.process_neighbour_buttons(4, 12)

    def click_pushButtonM6(self):
        if self.abrir(5, 12) == '0':
            self.process_neighbour_buttons(5, 12)

    def click_pushButtonM7(self):
        if self.abrir(6, 12) == '0':
            self.process_neighbour_buttons(6, 12)

    def click_pushButtonM8(self):
        if self.abrir(7, 12) == '0':
            self.process_neighbour_buttons(7, 12)

    def click_pushButtonM9(self):
        if self.abrir(8, 12) == '0':
            self.process_neighbour_buttons(8, 12)

    def click_pushButtonM10(self):
        if self.abrir(9, 12) == '0':
            self.process_neighbour_buttons(9, 12)

    def click_pushButtonM11(self):
        if self.abrir(10, 12) == '0':
            self.process_neighbour_buttons(10, 12)

    def click_pushButtonM12(self):
        if self.abrir(11, 12) == '0':
            self.process_neighbour_buttons(11, 12)

    def click_pushButtonM13(self):
        if self.abrir(12, 12) == '0':
            self.process_neighbour_buttons(12, 12)

    def click_pushButtonM14(self):
        if self.abrir(13, 12) == '0':
            self.process_neighbour_buttons(13, 12)

    def click_pushButtonM15(self):
        if self.abrir(14, 12) == '0':
            self.process_neighbour_buttons(14, 12)

    def click_pushButtonN1(self):
        if self.abrir(0, 13) == '0':
            self.process_neighbour_buttons(0, 13)

    def click_pushButtonN2(self):
        if self.abrir(1, 13) == '0':
            self.process_neighbour_buttons(1, 13)

    def click_pushButtonN3(self):
        if self.abrir(2, 13) == '0':
            self.process_neighbour_buttons(2, 13)

    def click_pushButtonN4(self):
        if self.abrir(3, 13) == '0':
            self.process_neighbour_buttons(3, 13)

    def click_pushButtonN5(self):
        if self.abrir(4, 13) == '0':
            self.process_neighbour_buttons(4, 13)

    def click_pushButtonN6(self):
        if self.abrir(5, 13) == '0':
            self.process_neighbour_buttons(5, 13)

    def click_pushButtonN7(self):
        if self.abrir(6, 13) == '0':
            self.process_neighbour_buttons(6, 13)

    def click_pushButtonN8(self):
        if self.abrir(7, 13) == '0':
            self.process_neighbour_buttons(7, 13)

    def click_pushButtonN9(self):
        if self.abrir(8, 13) == '0':
            self.process_neighbour_buttons(8, 13)

    def click_pushButtonN10(self):
        if self.abrir(9, 13) == '0':
            self.process_neighbour_buttons(9, 13)

    def click_pushButtonN11(self):
        if self.abrir(10, 13) == '0':
            self.process_neighbour_buttons(10, 13)

    def click_pushButtonN12(self):
        if self.abrir(11, 13) == '0':
            self.process_neighbour_buttons(11, 13)

    def click_pushButtonN13(self):
        if self.abrir(12, 13) == '0':
            self.process_neighbour_buttons(12, 13)

    def click_pushButtonN14(self):
        if self.abrir(13, 13) == '0':
            self.process_neighbour_buttons(13, 13)

    def click_pushButtonN15(self):
        if self.abrir(14, 13) == '0':
            self.process_neighbour_buttons(14, 13)

    def click_pushButtonO1(self):
        if self.abrir(0, 14) == '0':
            self.process_neighbour_buttons(0, 14)

    def click_pushButtonO2(self):
        if self.abrir(1, 14) == '0':
            self.process_neighbour_buttons(1, 14)

    def click_pushButtonO3(self):
        if self.abrir(2, 14) == '0':
            self.process_neighbour_buttons(2, 14)

    def click_pushButtonO4(self):
        if self.abrir(3, 14) == '0':
            self.process_neighbour_buttons(3, 14)

    def click_pushButtonO5(self):
        if self.abrir(4, 14) == '0':
            self.process_neighbour_buttons(4, 14)

    def click_pushButtonO6(self):
        if self.abrir(5, 14) == '0':
            self.process_neighbour_buttons(5, 14)

    def click_pushButtonO7(self):
        if self.abrir(6, 14) == '0':
            self.process_neighbour_buttons(6, 14)

    def click_pushButtonO8(self):
        if self.abrir(7, 14) == '0':
            self.process_neighbour_buttons(7, 14)

    def click_pushButtonO9(self):
        if self.abrir(8, 14) == '0':
            self.process_neighbour_buttons(8, 14)

    def click_pushButtonO10(self):
        if self.abrir(9, 14) == '0':
            self.process_neighbour_buttons(9, 14)

    def click_pushButtonO11(self):
        if self.abrir(10, 14) == '0':
            self.process_neighbour_buttons(10, 14)

    def click_pushButtonO12(self):
        if self.abrir(11, 14) == '0':
            self.process_neighbour_buttons(11, 14)

    def click_pushButtonO13(self):
        if self.abrir(12, 14) == '0':
            self.process_neighbour_buttons(12, 14)

    def click_pushButtonO14(self):
        if self.abrir(13, 14) == '0':
            self.process_neighbour_buttons(13, 14)

    def click_pushButtonO15(self):
        if self.abrir(14, 14) == '0':
            self.process_neighbour_buttons(14, 14)

    def abrir(self, x, y):
        icon = self.show_image(self.board[y][x].value)
        self.board[y][x].setIcon(icon)
        self.board[y][x].setIconSize(QSize(30, 30))
        self.board[y][x].setEnabled(False)
        return self.board[y][x].value

    def show_image(self, value):
        if value == 'b':
            icon = self.icons.get_icon_bomb()
        elif value == 'B':
            icon = self.icons.get_icon_bomb_exploded()
        elif value == '0':
            icon = self.icons.get_icon_blank()
        elif value == '1':
            icon = self.icons.get_icon_number_1()
        elif value == '2':
            icon = self.icons.get_icon_number_2()
        elif value == '3':
            icon = self.icons.get_icon_number_3()
        elif value == '4':
            icon = self.icons.get_icon_number_4()
        elif value == '5':
            icon = self.icons.get_icon_number_5()
        elif value == '6':
            icon = self.icons.get_icon_number_6()
        elif value == '7':
            icon = self.icons.get_icon_number_7()
        elif value == '8':
            icon = self.icons.get_icon_number_8()
        else:
            raise "Invalid value"
        return icon

    def bombs_position_raffle(self):
        quant_bombs = 0
        while quant_bombs < Ui_MainWindow.QUANTITY_BOMBS:
            x = randint(0, Ui_MainWindow.LENGTH_AXIS_X - 1)
            y = randint(0, Ui_MainWindow.LENGTH_AXIS_Y - 1)
            print(x, y)
            if self.board[y][x].value != "b":
                self.board[y][x].value = "b"
                quant_bombs += 1

    def define_other_fields(self):
        for y in range(0, Ui_MainWindow.LENGTH_AXIS_Y):
            for x in range(0, Ui_MainWindow.LENGTH_AXIS_X):
                if self.board[y][x].value != 'b':
                    count_bombs = 0
                    for i in range(y - 1, y + 2):
                        for j in range(x - 1, x + 2):
                            if not ((i, j) == (y, x) or i < 0 or j < 0 or i >= Ui_MainWindow.LENGTH_AXIS_Y or
                                    j >= Ui_MainWindow.LENGTH_AXIS_X):
                                if self.board[i][j].value == 'b':
                                    count_bombs += 1
                    self.board[y][x].value = str(count_bombs)


class CriarTelaPrincipal(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(CriarTelaPrincipal, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        event.accept()
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CriarTelaPrincipal()
    window.show()
    sys.exit(app.exec_())
