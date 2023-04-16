import sys
from random import randint
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Button import Button


class Ui_MainWindow(object):
    # Constants
    LENGTH_AXIS_X = 15
    LENGTH_AXIS_Y = 15
    QUANTITY_BOMBS = 20

    def __init__(self):
        self.centralwidget = QWidget()
        # First line
        self.pushButtonA1 = Button()
        self.pushButtonA2 = Button()
        self.pushButtonA3 = Button()
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
        self.pushButtonB1 = Button()
        self.pushButtonB2 = Button()
        self.pushButtonB3 = Button()
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
        self.pushButtonC1 = Button()
        self.pushButtonC2 = Button()
        self.pushButtonC3 = Button()
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
        self.pushButtonA1 = Button(self.centralwidget, QRect(10, 30, 30, 30))
        self.pushButtonA2 = Button(self.centralwidget, QRect(40, 30, 30, 30))
        self.pushButtonA3 = Button(self.centralwidget, QRect(70, 30, 30, 30))
        self.pushButtonA4 = Button(self.centralwidget, QRect(100, 30, 30, 30))
        self.pushButtonA5 = Button(self.centralwidget, QRect(130, 30, 30, 30))
        self.pushButtonA6 = Button(self.centralwidget, QRect(160, 30, 30, 30))
        self.pushButtonA7 = Button(self.centralwidget, QRect(190, 30, 30, 30))
        self.pushButtonA8 = Button(self.centralwidget, QRect(220, 30, 30, 30))
        self.pushButtonA9 = Button(self.centralwidget, QRect(250, 30, 30, 30))
        self.pushButtonA10 = Button(self.centralwidget, QRect(280, 30, 30, 30))
        self.pushButtonA11 = Button(self.centralwidget, QRect(310, 30, 30, 30))
        self.pushButtonA12 = Button(self.centralwidget, QRect(340, 30, 30, 30))
        self.pushButtonA13 = Button(self.centralwidget, QRect(370, 30, 30, 30))
        self.pushButtonA14 = Button(self.centralwidget, QRect(400, 30, 30, 30))
        self.pushButtonA15 = Button(self.centralwidget, QRect(430, 30, 30, 30))
        # Second line
        self.pushButtonB1 = Button(self.centralwidget, QRect(10, 60, 30, 30))
        self.pushButtonB2 = Button(self.centralwidget, QRect(40, 60, 30, 30))
        self.pushButtonB3 = Button(self.centralwidget, QRect(70, 60, 30, 30))
        self.pushButtonB4 = Button(self.centralwidget, QRect(100, 60, 30, 30))
        self.pushButtonB5 = Button(self.centralwidget, QRect(130, 60, 30, 30))
        self.pushButtonB6 = Button(self.centralwidget, QRect(160, 60, 30, 30))
        self.pushButtonB7 = Button(self.centralwidget, QRect(190, 60, 30, 30))
        self.pushButtonB8 = Button(self.centralwidget, QRect(220, 60, 30, 30))
        self.pushButtonB9 = Button(self.centralwidget, QRect(250, 60, 30, 30))
        self.pushButtonB10 = Button(self.centralwidget, QRect(280, 60, 30, 30))
        self.pushButtonB11 = Button(self.centralwidget, QRect(310, 60, 30, 30))
        self.pushButtonB12 = Button(self.centralwidget, QRect(340, 60, 30, 30))
        self.pushButtonB13 = Button(self.centralwidget, QRect(370, 60, 30, 30))
        self.pushButtonB14 = Button(self.centralwidget, QRect(400, 60, 30, 30))
        self.pushButtonB15 = Button(self.centralwidget, QRect(430, 60, 30, 30))
        # Third line
        self.pushButtonC1 = Button(self.centralwidget, QRect(10, 90, 30, 30))
        self.pushButtonC2 = Button(self.centralwidget, QRect(40, 90, 30, 30))
        self.pushButtonC3 = Button(self.centralwidget, QRect(70, 90, 30, 30))
        self.pushButtonC4 = Button(self.centralwidget, QRect(100, 90, 30, 30))
        self.pushButtonC5 = Button(self.centralwidget, QRect(130, 90, 30, 30))
        self.pushButtonC6 = Button(self.centralwidget, QRect(160, 90, 30, 30))
        self.pushButtonC7 = Button(self.centralwidget, QRect(190, 90, 30, 30))
        self.pushButtonC8 = Button(self.centralwidget, QRect(220, 90, 30, 30))
        self.pushButtonC9 = Button(self.centralwidget, QRect(250, 90, 30, 30))
        self.pushButtonC10 = Button(self.centralwidget, QRect(280, 90, 30, 30))
        self.pushButtonC11 = Button(self.centralwidget, QRect(310, 90, 30, 30))
        self.pushButtonC12 = Button(self.centralwidget, QRect(340, 90, 30, 30))
        self.pushButtonC13 = Button(self.centralwidget, QRect(370, 90, 30, 30))
        self.pushButtonC14 = Button(self.centralwidget, QRect(400, 90, 30, 30))
        self.pushButtonC15 = Button(self.centralwidget, QRect(430, 90, 30, 30))
        # Fourth line
        self.pushButtonD1 = Button(self.centralwidget, QRect(10, 120, 30, 30))
        self.pushButtonD2 = Button(self.centralwidget, QRect(40, 120, 30, 30))
        self.pushButtonD3 = Button(self.centralwidget, QRect(70, 120, 30, 30))
        self.pushButtonD4 = Button(self.centralwidget, QRect(100, 120, 30, 30))
        self.pushButtonD5 = Button(self.centralwidget, QRect(130, 120, 30, 30))
        self.pushButtonD6 = Button(self.centralwidget, QRect(160, 120, 30, 30))
        self.pushButtonD7 = Button(self.centralwidget, QRect(190, 120, 30, 30))
        self.pushButtonD8 = Button(self.centralwidget, QRect(220, 120, 30, 30))
        self.pushButtonD9 = Button(self.centralwidget, QRect(250, 120, 30, 30))
        self.pushButtonD10 = Button(self.centralwidget, QRect(280, 120, 30, 30))
        self.pushButtonD11 = Button(self.centralwidget, QRect(310, 120, 30, 30))
        self.pushButtonD12 = Button(self.centralwidget, QRect(340, 120, 30, 30))
        self.pushButtonD13 = Button(self.centralwidget, QRect(370, 120, 30, 30))
        self.pushButtonD14 = Button(self.centralwidget, QRect(400, 120, 30, 30))
        self.pushButtonD15 = Button(self.centralwidget, QRect(430, 120, 30, 30))
        # Fiveth line
        self.pushButtonE1 = Button(self.centralwidget, QRect(10, 150, 30, 30))
        self.pushButtonE2 = Button(self.centralwidget, QRect(40, 150, 30, 30))
        self.pushButtonE3 = Button(self.centralwidget, QRect(70, 150, 30, 30))
        self.pushButtonE4 = Button(self.centralwidget, QRect(100, 150, 30, 30))
        self.pushButtonE5 = Button(self.centralwidget, QRect(130, 150, 30, 30))
        self.pushButtonE6 = Button(self.centralwidget, QRect(160, 150, 30, 30))
        self.pushButtonE7 = Button(self.centralwidget, QRect(190, 150, 30, 30))
        self.pushButtonE8 = Button(self.centralwidget, QRect(220, 150, 30, 30))
        self.pushButtonE9 = Button(self.centralwidget, QRect(250, 150, 30, 30))
        self.pushButtonE10 = Button(self.centralwidget, QRect(280, 150, 30, 30))
        self.pushButtonE11 = Button(self.centralwidget, QRect(310, 150, 30, 30))
        self.pushButtonE12 = Button(self.centralwidget, QRect(340, 150, 30, 30))
        self.pushButtonE13 = Button(self.centralwidget, QRect(370, 150, 30, 30))
        self.pushButtonE14 = Button(self.centralwidget, QRect(400, 150, 30, 30))
        self.pushButtonE15 = Button(self.centralwidget, QRect(430, 150, 30, 30))
        # Sixth line
        self.pushButtonF1 = Button(self.centralwidget, QRect(10, 180, 30, 30))
        self.pushButtonF2 = Button(self.centralwidget, QRect(40, 180, 30, 30))
        self.pushButtonF3 = Button(self.centralwidget, QRect(70, 180, 30, 30))
        self.pushButtonF4 = Button(self.centralwidget, QRect(100, 180, 30, 30))
        self.pushButtonF5 = Button(self.centralwidget, QRect(130, 180, 30, 30))
        self.pushButtonF6 = Button(self.centralwidget, QRect(160, 180, 30, 30))
        self.pushButtonF7 = Button(self.centralwidget, QRect(190, 180, 30, 30))
        self.pushButtonF8 = Button(self.centralwidget, QRect(220, 180, 30, 30))
        self.pushButtonF9 = Button(self.centralwidget, QRect(250, 180, 30, 30))
        self.pushButtonF10 = Button(self.centralwidget, QRect(280, 180, 30, 30))
        self.pushButtonF11 = Button(self.centralwidget, QRect(310, 180, 30, 30))
        self.pushButtonF12 = Button(self.centralwidget, QRect(340, 180, 30, 30))
        self.pushButtonF13 = Button(self.centralwidget, QRect(370, 180, 30, 30))
        self.pushButtonF14 = Button(self.centralwidget, QRect(400, 180, 30, 30))
        self.pushButtonF15 = Button(self.centralwidget, QRect(430, 180, 30, 30))
        # Seventh line
        self.pushButtonG1 = Button(self.centralwidget, QRect(10, 210, 30, 30))
        self.pushButtonG2 = Button(self.centralwidget, QRect(40, 210, 30, 30))
        self.pushButtonG3 = Button(self.centralwidget, QRect(70, 210, 30, 30))
        self.pushButtonG4 = Button(self.centralwidget, QRect(100, 210, 30, 30))
        self.pushButtonG5 = Button(self.centralwidget, QRect(130, 210, 30, 30))
        self.pushButtonG6 = Button(self.centralwidget, QRect(160, 210, 30, 30))
        self.pushButtonG7 = Button(self.centralwidget, QRect(190, 210, 30, 30))
        self.pushButtonG8 = Button(self.centralwidget, QRect(220, 210, 30, 30))
        self.pushButtonG9 = Button(self.centralwidget, QRect(250, 210, 30, 30))
        self.pushButtonG10 = Button(self.centralwidget, QRect(280, 210, 30, 30))
        self.pushButtonG11 = Button(self.centralwidget, QRect(310, 210, 30, 30))
        self.pushButtonG12 = Button(self.centralwidget, QRect(340, 210, 30, 30))
        self.pushButtonG13 = Button(self.centralwidget, QRect(370, 210, 30, 30))
        self.pushButtonG14 = Button(self.centralwidget, QRect(400, 210, 30, 30))
        self.pushButtonG15 = Button(self.centralwidget, QRect(430, 210, 30, 30))
        # Eighth line
        self.pushButtonH1 = Button(self.centralwidget, QRect(10, 240, 30, 30))
        self.pushButtonH2 = Button(self.centralwidget, QRect(40, 240, 30, 30))
        self.pushButtonH3 = Button(self.centralwidget, QRect(70, 240, 30, 30))
        self.pushButtonH4 = Button(self.centralwidget, QRect(100, 240, 30, 30))
        self.pushButtonH5 = Button(self.centralwidget, QRect(130, 240, 30, 30))
        self.pushButtonH6 = Button(self.centralwidget, QRect(160, 240, 30, 30))
        self.pushButtonH7 = Button(self.centralwidget, QRect(190, 240, 30, 30))
        self.pushButtonH8 = Button(self.centralwidget, QRect(220, 240, 30, 30))
        self.pushButtonH9 = Button(self.centralwidget, QRect(250, 240, 30, 30))
        self.pushButtonH10 = Button(self.centralwidget, QRect(280, 240, 30, 30))
        self.pushButtonH11 = Button(self.centralwidget, QRect(310, 240, 30, 30))
        self.pushButtonH12 = Button(self.centralwidget, QRect(340, 240, 30, 30))
        self.pushButtonH13 = Button(self.centralwidget, QRect(370, 240, 30, 30))
        self.pushButtonH14 = Button(self.centralwidget, QRect(400, 240, 30, 30))
        self.pushButtonH15 = Button(self.centralwidget, QRect(430, 240, 30, 30))
        # Nineth line
        self.pushButtonI1 = Button(self.centralwidget, QRect(10, 270, 30, 30))
        self.pushButtonI2 = Button(self.centralwidget, QRect(40, 270, 30, 30))
        self.pushButtonI3 = Button(self.centralwidget, QRect(70, 270, 30, 30))
        self.pushButtonI4 = Button(self.centralwidget, QRect(100, 270, 30, 30))
        self.pushButtonI5 = Button(self.centralwidget, QRect(130, 270, 30, 30))
        self.pushButtonI6 = Button(self.centralwidget, QRect(160, 270, 30, 30))
        self.pushButtonI7 = Button(self.centralwidget, QRect(190, 270, 30, 30))
        self.pushButtonI8 = Button(self.centralwidget, QRect(220, 270, 30, 30))
        self.pushButtonI9 = Button(self.centralwidget, QRect(250, 270, 30, 30))
        self.pushButtonI10 = Button(self.centralwidget, QRect(280, 270, 30, 30))
        self.pushButtonI11 = Button(self.centralwidget, QRect(310, 270, 30, 30))
        self.pushButtonI12 = Button(self.centralwidget, QRect(340, 270, 30, 30))
        self.pushButtonI13 = Button(self.centralwidget, QRect(370, 270, 30, 30))
        self.pushButtonI14 = Button(self.centralwidget, QRect(400, 270, 30, 30))
        self.pushButtonI15 = Button(self.centralwidget, QRect(430, 270, 30, 30))
        # Tenth line
        self.pushButtonJ1 = Button(self.centralwidget, QRect(10, 300, 30, 30))
        self.pushButtonJ2 = Button(self.centralwidget, QRect(40, 300, 30, 30))
        self.pushButtonJ3 = Button(self.centralwidget, QRect(70, 300, 30, 30))
        self.pushButtonJ4 = Button(self.centralwidget, QRect(100, 300, 30, 30))
        self.pushButtonJ5 = Button(self.centralwidget, QRect(130, 300, 30, 30))
        self.pushButtonJ6 = Button(self.centralwidget, QRect(160, 300, 30, 30))
        self.pushButtonJ7 = Button(self.centralwidget, QRect(190, 300, 30, 30))
        self.pushButtonJ8 = Button(self.centralwidget, QRect(220, 300, 30, 30))
        self.pushButtonJ9 = Button(self.centralwidget, QRect(250, 300, 30, 30))
        self.pushButtonJ10 = Button(self.centralwidget, QRect(280, 300, 30, 30))
        self.pushButtonJ11 = Button(self.centralwidget, QRect(310, 300, 30, 30))
        self.pushButtonJ12 = Button(self.centralwidget, QRect(340, 300, 30, 30))
        self.pushButtonJ13 = Button(self.centralwidget, QRect(370, 300, 30, 30))
        self.pushButtonJ14 = Button(self.centralwidget, QRect(400, 300, 30, 30))
        self.pushButtonJ15 = Button(self.centralwidget, QRect(430, 300, 30, 30))
        # Eleventh line
        self.pushButtonK1 = Button(self.centralwidget, QRect(10, 330, 30, 30))
        self.pushButtonK2 = Button(self.centralwidget, QRect(40, 330, 30, 30))
        self.pushButtonK3 = Button(self.centralwidget, QRect(70, 330, 30, 30))
        self.pushButtonK4 = Button(self.centralwidget, QRect(100, 330, 30, 30))
        self.pushButtonK5 = Button(self.centralwidget, QRect(130, 330, 30, 30))
        self.pushButtonK6 = Button(self.centralwidget, QRect(160, 330, 30, 30))
        self.pushButtonK7 = Button(self.centralwidget, QRect(190, 330, 30, 30))
        self.pushButtonK8 = Button(self.centralwidget, QRect(220, 330, 30, 30))
        self.pushButtonK9 = Button(self.centralwidget, QRect(250, 330, 30, 30))
        self.pushButtonK10 = Button(self.centralwidget, QRect(280, 330, 30, 30))
        self.pushButtonK11 = Button(self.centralwidget, QRect(310, 330, 30, 30))
        self.pushButtonK12 = Button(self.centralwidget, QRect(340, 330, 30, 30))
        self.pushButtonK13 = Button(self.centralwidget, QRect(370, 330, 30, 30))
        self.pushButtonK14 = Button(self.centralwidget, QRect(400, 330, 30, 30))
        self.pushButtonK15 = Button(self.centralwidget, QRect(430, 330, 30, 30))
        # Twelveth line
        self.pushButtonL1 = Button(self.centralwidget, QRect(10, 360, 30, 30))
        self.pushButtonL2 = Button(self.centralwidget, QRect(40, 360, 30, 30))
        self.pushButtonL3 = Button(self.centralwidget, QRect(70, 360, 30, 30))
        self.pushButtonL4 = Button(self.centralwidget, QRect(100, 360, 30, 30))
        self.pushButtonL5 = Button(self.centralwidget, QRect(130, 360, 30, 30))
        self.pushButtonL6 = Button(self.centralwidget, QRect(160, 360, 30, 30))
        self.pushButtonL7 = Button(self.centralwidget, QRect(190, 360, 30, 30))
        self.pushButtonL8 = Button(self.centralwidget, QRect(220, 360, 30, 30))
        self.pushButtonL9 = Button(self.centralwidget, QRect(250, 360, 30, 30))
        self.pushButtonL10 = Button(self.centralwidget, QRect(280, 360, 30, 30))
        self.pushButtonL11 = Button(self.centralwidget, QRect(310, 360, 30, 30))
        self.pushButtonL12 = Button(self.centralwidget, QRect(340, 360, 30, 30))
        self.pushButtonL13 = Button(self.centralwidget, QRect(370, 360, 30, 30))
        self.pushButtonL14 = Button(self.centralwidget, QRect(400, 360, 30, 30))
        self.pushButtonL15 = Button(self.centralwidget, QRect(430, 360, 30, 30))
        # Thirteenth line
        self.pushButtonM1 = Button(self.centralwidget, QRect(10, 390, 30, 30))
        self.pushButtonM2 = Button(self.centralwidget, QRect(40, 390, 30, 30))
        self.pushButtonM3 = Button(self.centralwidget, QRect(70, 390, 30, 30))
        self.pushButtonM4 = Button(self.centralwidget, QRect(100, 390, 30, 30))
        self.pushButtonM5 = Button(self.centralwidget, QRect(130, 390, 30, 30))
        self.pushButtonM6 = Button(self.centralwidget, QRect(160, 390, 30, 30))
        self.pushButtonM7 = Button(self.centralwidget, QRect(190, 390, 30, 30))
        self.pushButtonM8 = Button(self.centralwidget, QRect(220, 390, 30, 30))
        self.pushButtonM9 = Button(self.centralwidget, QRect(250, 390, 30, 30))
        self.pushButtonM10 = Button(self.centralwidget, QRect(280, 390, 30, 30))
        self.pushButtonM11 = Button(self.centralwidget, QRect(310, 390, 30, 30))
        self.pushButtonM12 = Button(self.centralwidget, QRect(340, 390, 30, 30))
        self.pushButtonM13 = Button(self.centralwidget, QRect(370, 390, 30, 30))
        self.pushButtonM14 = Button(self.centralwidget, QRect(400, 390, 30, 30))
        self.pushButtonM15 = Button(self.centralwidget, QRect(430, 390, 30, 30))
        # Fourteenth line
        self.pushButtonN1 = Button(self.centralwidget, QRect(10, 420, 30, 30))
        self.pushButtonN2 = Button(self.centralwidget, QRect(40, 420, 30, 30))
        self.pushButtonN3 = Button(self.centralwidget, QRect(70, 420, 30, 30))
        self.pushButtonN4 = Button(self.centralwidget, QRect(100, 420, 30, 30))
        self.pushButtonN5 = Button(self.centralwidget, QRect(130, 420, 30, 30))
        self.pushButtonN6 = Button(self.centralwidget, QRect(160, 420, 30, 30))
        self.pushButtonN7 = Button(self.centralwidget, QRect(190, 420, 30, 30))
        self.pushButtonN8 = Button(self.centralwidget, QRect(220, 420, 30, 30))
        self.pushButtonN9 = Button(self.centralwidget, QRect(250, 420, 30, 30))
        self.pushButtonN10 = Button(self.centralwidget, QRect(280, 420, 30, 30))
        self.pushButtonN11 = Button(self.centralwidget, QRect(310, 420, 30, 30))
        self.pushButtonN12 = Button(self.centralwidget, QRect(340, 420, 30, 30))
        self.pushButtonN13 = Button(self.centralwidget, QRect(370, 420, 30, 30))
        self.pushButtonN14 = Button(self.centralwidget, QRect(400, 420, 30, 30))
        self.pushButtonN15 = Button(self.centralwidget, QRect(430, 420, 30, 30))
        # Fiveteenth line
        self.pushButtonO1 = Button(self.centralwidget, QRect(10, 450, 30, 30))
        self.pushButtonO2 = Button(self.centralwidget, QRect(40, 450, 30, 30))
        self.pushButtonO3 = Button(self.centralwidget, QRect(70, 450, 30, 30))
        self.pushButtonO4 = Button(self.centralwidget, QRect(100, 450, 30, 30))
        self.pushButtonO5 = Button(self.centralwidget, QRect(130, 450, 30, 30))
        self.pushButtonO6 = Button(self.centralwidget, QRect(160, 450, 30, 30))
        self.pushButtonO7 = Button(self.centralwidget, QRect(190, 450, 30, 30))
        self.pushButtonO8 = Button(self.centralwidget, QRect(220, 450, 30, 30))
        self.pushButtonO9 = Button(self.centralwidget, QRect(250, 450, 30, 30))
        self.pushButtonO10 = Button(self.centralwidget, QRect(280, 450, 30, 30))
        self.pushButtonO11 = Button(self.centralwidget, QRect(310, 450, 30, 30))
        self.pushButtonO12 = Button(self.centralwidget, QRect(340, 450, 30, 30))
        self.pushButtonO13 = Button(self.centralwidget, QRect(370, 450, 30, 30))
        self.pushButtonO14 = Button(self.centralwidget, QRect(400, 450, 30, 30))
        self.pushButtonO15 = Button(self.centralwidget, QRect(430, 450, 30, 30))

        MainWindow.setCentralWidget(self.centralwidget)

        self.create_board()
        self.bombs_position_raffle()
        self.define_other_fields()

    def bombs_position_raffle(self):
        quant_bombs = 0
        while quant_bombs < Ui_MainWindow.QUANTITY_BOMBS:
            x = randint(0, Ui_MainWindow.LENGTH_AXIS_X - 1)
            y = randint(0, Ui_MainWindow.LENGTH_AXIS_Y - 1)
            if self.board[y][x].get_value() == "0":
                self.board[y][x].set_value("b")
                print(x, y)
                quant_bombs += 1

    def define_other_fields(self):
        for y in range(0, Ui_MainWindow.LENGTH_AXIS_Y):
            for x in range(0, Ui_MainWindow.LENGTH_AXIS_X):
                if self.board[y][x].get_value() != 'b':
                    count_bombs = 0
                    for i in range(y - 1, y + 2):
                        for j in range(x - 1, x + 2):
                            if not ((i, j) == (y, x) or i < 0 or j < 0 or i >= Ui_MainWindow.LENGTH_AXIS_Y or
                                    j >= Ui_MainWindow.LENGTH_AXIS_X):
                                if self.board[i][j].get_value() == 'b':
                                    count_bombs += 1
                    print(count_bombs)
                    self.board[y][x].set_value(str(count_bombs))


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
