import sys
from random import randint

from PySide2 import QtCore
from PySide2.QtGui import QCursor, QMouseEvent
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from Icon import Icon


class Ui_MainWindow(object):
    # Constants
    LENGTH_AXIS_X = 15
    LENGTH_AXIS_Y = 15
    QUANTITY_BOMBS = 40
    QUANTITY_FIELDS = (LENGTH_AXIS_X * LENGTH_AXIS_Y) - QUANTITY_BOMBS
    VICTORY = 1
    DEFEAT = 2

    def __init__(self):
        # Init central widget
        self.centralwidget = QWidget()
        # Init icons
        self.icons = Icon()
        # Init label bombs
        self.bombs_label = QLabel()
        self.bombs_label_2 = QLabel()
        self.buttons_flagged = 0
        # Init timer
        self.time = QTime()
        self.timer_label = QLabel()
        self.timer = QTimer()
        self.timer_label_2 = QLabel()
        # First line
        self.pushButtonA1 = QPushButton()
        self.pushButtonA2 = QPushButton()
        self.pushButtonA3 = QPushButton()
        self.pushButtonA4 = QPushButton()
        self.pushButtonA5 = QPushButton()
        self.pushButtonA6 = QPushButton()
        self.pushButtonA7 = QPushButton()
        self.pushButtonA8 = QPushButton()
        self.pushButtonA9 = QPushButton()
        self.pushButtonA10 = QPushButton()
        self.pushButtonA11 = QPushButton()
        self.pushButtonA12 = QPushButton()
        self.pushButtonA13 = QPushButton()
        self.pushButtonA14 = QPushButton()
        self.pushButtonA15 = QPushButton()
        # Second line
        self.pushButtonB1 = QPushButton()
        self.pushButtonB2 = QPushButton()
        self.pushButtonB3 = QPushButton()
        self.pushButtonB4 = QPushButton()
        self.pushButtonB5 = QPushButton()
        self.pushButtonB6 = QPushButton()
        self.pushButtonB7 = QPushButton()
        self.pushButtonB8 = QPushButton()
        self.pushButtonB9 = QPushButton()
        self.pushButtonB10 = QPushButton()
        self.pushButtonB11 = QPushButton()
        self.pushButtonB12 = QPushButton()
        self.pushButtonB13 = QPushButton()
        self.pushButtonB14 = QPushButton()
        self.pushButtonB15 = QPushButton()
        # Third line
        self.pushButtonC1 = QPushButton()
        self.pushButtonC2 = QPushButton()
        self.pushButtonC3 = QPushButton()
        self.pushButtonC4 = QPushButton()
        self.pushButtonC5 = QPushButton()
        self.pushButtonC6 = QPushButton()
        self.pushButtonC7 = QPushButton()
        self.pushButtonC8 = QPushButton()
        self.pushButtonC9 = QPushButton()
        self.pushButtonC10 = QPushButton()
        self.pushButtonC11 = QPushButton()
        self.pushButtonC12 = QPushButton()
        self.pushButtonC13 = QPushButton()
        self.pushButtonC14 = QPushButton()
        self.pushButtonC15 = QPushButton()
        # Fourth line
        self.pushButtonD1 = QPushButton()
        self.pushButtonD2 = QPushButton()
        self.pushButtonD3 = QPushButton()
        self.pushButtonD4 = QPushButton()
        self.pushButtonD5 = QPushButton()
        self.pushButtonD6 = QPushButton()
        self.pushButtonD7 = QPushButton()
        self.pushButtonD8 = QPushButton()
        self.pushButtonD9 = QPushButton()
        self.pushButtonD10 = QPushButton()
        self.pushButtonD11 = QPushButton()
        self.pushButtonD12 = QPushButton()
        self.pushButtonD13 = QPushButton()
        self.pushButtonD14 = QPushButton()
        self.pushButtonD15 = QPushButton()
        # Fiveth line
        self.pushButtonE1 = QPushButton()
        self.pushButtonE2 = QPushButton()
        self.pushButtonE3 = QPushButton()
        self.pushButtonE4 = QPushButton()
        self.pushButtonE5 = QPushButton()
        self.pushButtonE6 = QPushButton()
        self.pushButtonE7 = QPushButton()
        self.pushButtonE8 = QPushButton()
        self.pushButtonE9 = QPushButton()
        self.pushButtonE10 = QPushButton()
        self.pushButtonE11 = QPushButton()
        self.pushButtonE12 = QPushButton()
        self.pushButtonE13 = QPushButton()
        self.pushButtonE14 = QPushButton()
        self.pushButtonE15 = QPushButton()
        # Sixth line
        self.pushButtonF1 = QPushButton()
        self.pushButtonF2 = QPushButton()
        self.pushButtonF3 = QPushButton()
        self.pushButtonF4 = QPushButton()
        self.pushButtonF5 = QPushButton()
        self.pushButtonF6 = QPushButton()
        self.pushButtonF7 = QPushButton()
        self.pushButtonF8 = QPushButton()
        self.pushButtonF9 = QPushButton()
        self.pushButtonF10 = QPushButton()
        self.pushButtonF11 = QPushButton()
        self.pushButtonF12 = QPushButton()
        self.pushButtonF13 = QPushButton()
        self.pushButtonF14 = QPushButton()
        self.pushButtonF15 = QPushButton()
        # Seventh line
        self.pushButtonG1 = QPushButton()
        self.pushButtonG2 = QPushButton()
        self.pushButtonG3 = QPushButton()
        self.pushButtonG4 = QPushButton()
        self.pushButtonG5 = QPushButton()
        self.pushButtonG6 = QPushButton()
        self.pushButtonG7 = QPushButton()
        self.pushButtonG8 = QPushButton()
        self.pushButtonG9 = QPushButton()
        self.pushButtonG10 = QPushButton()
        self.pushButtonG11 = QPushButton()
        self.pushButtonG12 = QPushButton()
        self.pushButtonG13 = QPushButton()
        self.pushButtonG14 = QPushButton()
        self.pushButtonG15 = QPushButton()
        # Eighth line
        self.pushButtonH1 = QPushButton()
        self.pushButtonH2 = QPushButton()
        self.pushButtonH3 = QPushButton()
        self.pushButtonH4 = QPushButton()
        self.pushButtonH5 = QPushButton()
        self.pushButtonH6 = QPushButton()
        self.pushButtonH7 = QPushButton()
        self.pushButtonH8 = QPushButton()
        self.pushButtonH9 = QPushButton()
        self.pushButtonH10 = QPushButton()
        self.pushButtonH11 = QPushButton()
        self.pushButtonH12 = QPushButton()
        self.pushButtonH13 = QPushButton()
        self.pushButtonH14 = QPushButton()
        self.pushButtonH15 = QPushButton()
        # Nineth line
        self.pushButtonI1 = QPushButton()
        self.pushButtonI2 = QPushButton()
        self.pushButtonI3 = QPushButton()
        self.pushButtonI4 = QPushButton()
        self.pushButtonI5 = QPushButton()
        self.pushButtonI6 = QPushButton()
        self.pushButtonI7 = QPushButton()
        self.pushButtonI8 = QPushButton()
        self.pushButtonI9 = QPushButton()
        self.pushButtonI10 = QPushButton()
        self.pushButtonI11 = QPushButton()
        self.pushButtonI12 = QPushButton()
        self.pushButtonI13 = QPushButton()
        self.pushButtonI14 = QPushButton()
        self.pushButtonI15 = QPushButton()
        # Tenth line
        self.pushButtonJ1 = QPushButton()
        self.pushButtonJ2 = QPushButton()
        self.pushButtonJ3 = QPushButton()
        self.pushButtonJ4 = QPushButton()
        self.pushButtonJ5 = QPushButton()
        self.pushButtonJ6 = QPushButton()
        self.pushButtonJ7 = QPushButton()
        self.pushButtonJ8 = QPushButton()
        self.pushButtonJ9 = QPushButton()
        self.pushButtonJ10 = QPushButton()
        self.pushButtonJ11 = QPushButton()
        self.pushButtonJ12 = QPushButton()
        self.pushButtonJ13 = QPushButton()
        self.pushButtonJ14 = QPushButton()
        self.pushButtonJ15 = QPushButton()
        # Eleventh line
        self.pushButtonK1 = QPushButton()
        self.pushButtonK2 = QPushButton()
        self.pushButtonK3 = QPushButton()
        self.pushButtonK4 = QPushButton()
        self.pushButtonK5 = QPushButton()
        self.pushButtonK6 = QPushButton()
        self.pushButtonK7 = QPushButton()
        self.pushButtonK8 = QPushButton()
        self.pushButtonK9 = QPushButton()
        self.pushButtonK10 = QPushButton()
        self.pushButtonK11 = QPushButton()
        self.pushButtonK12 = QPushButton()
        self.pushButtonK13 = QPushButton()
        self.pushButtonK14 = QPushButton()
        self.pushButtonK15 = QPushButton()
        # Twelveth line
        self.pushButtonL1 = QPushButton()
        self.pushButtonL2 = QPushButton()
        self.pushButtonL3 = QPushButton()
        self.pushButtonL4 = QPushButton()
        self.pushButtonL5 = QPushButton()
        self.pushButtonL6 = QPushButton()
        self.pushButtonL7 = QPushButton()
        self.pushButtonL8 = QPushButton()
        self.pushButtonL9 = QPushButton()
        self.pushButtonL10 = QPushButton()
        self.pushButtonL11 = QPushButton()
        self.pushButtonL12 = QPushButton()
        self.pushButtonL13 = QPushButton()
        self.pushButtonL14 = QPushButton()
        self.pushButtonL15 = QPushButton()
        # Thirteenth line
        self.pushButtonM1 = QPushButton()
        self.pushButtonM2 = QPushButton()
        self.pushButtonM3 = QPushButton()
        self.pushButtonM4 = QPushButton()
        self.pushButtonM5 = QPushButton()
        self.pushButtonM6 = QPushButton()
        self.pushButtonM7 = QPushButton()
        self.pushButtonM8 = QPushButton()
        self.pushButtonM9 = QPushButton()
        self.pushButtonM10 = QPushButton()
        self.pushButtonM11 = QPushButton()
        self.pushButtonM12 = QPushButton()
        self.pushButtonM13 = QPushButton()
        self.pushButtonM14 = QPushButton()
        self.pushButtonM15 = QPushButton()
        # Fourteenth line
        self.pushButtonN1 = QPushButton()
        self.pushButtonN2 = QPushButton()
        self.pushButtonN3 = QPushButton()
        self.pushButtonN4 = QPushButton()
        self.pushButtonN5 = QPushButton()
        self.pushButtonN6 = QPushButton()
        self.pushButtonN7 = QPushButton()
        self.pushButtonN8 = QPushButton()
        self.pushButtonN9 = QPushButton()
        self.pushButtonN10 = QPushButton()
        self.pushButtonN11 = QPushButton()
        self.pushButtonN12 = QPushButton()
        self.pushButtonN13 = QPushButton()
        self.pushButtonN14 = QPushButton()
        self.pushButtonN15 = QPushButton()
        # Fiveteenth line
        self.pushButtonO1 = QPushButton()
        self.pushButtonO2 = QPushButton()
        self.pushButtonO3 = QPushButton()
        self.pushButtonO4 = QPushButton()
        self.pushButtonO5 = QPushButton()
        self.pushButtonO6 = QPushButton()
        self.pushButtonO7 = QPushButton()
        self.pushButtonO8 = QPushButton()
        self.pushButtonO9 = QPushButton()
        self.pushButtonO10 = QPushButton()
        self.pushButtonO11 = QPushButton()
        self.pushButtonO12 = QPushButton()
        self.pushButtonO13 = QPushButton()
        self.pushButtonO14 = QPushButton()
        self.pushButtonO15 = QPushButton()
        # Init list button functions
        self.function_click_buttons = []
        # Init board
        self.board = []
        # Init button flag
        self.pushButtonFlag = QPushButton()
        # Init label flag
        self.flag_label = QLabel()

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
              self.pushButtonO11, self.pushButtonO12, self.pushButtonO13, self.pushButtonO14, self.pushButtonO15]]

    def create_button_functions(self):
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

    def setupUi(self, MainWindow):
        # Create icons
        self.icons = Icon()
        # Create main window
        MainWindow.resize(470, 550)
        MainWindow.setMaximumSize(470, 550)
        MainWindow.setMinimumSize(470, 550)
        MainWindow.setWindowTitle("Minefield")
        MainWindow.setWindowIcon(self.icons.get_icon_bomb())
        # Create central widget
        self.centralwidget = QWidget()
        # First line
        self.pushButtonA1 = QPushButton(self.centralwidget)
        self.pushButtonA1.setGeometry(QRect(10, 10, 30, 30))
        self.pushButtonA2 = QPushButton(self.centralwidget)
        self.pushButtonA2.setGeometry(QRect(40, 10, 30, 30))
        self.pushButtonA3 = QPushButton(self.centralwidget)
        self.pushButtonA3.setGeometry(QRect(70, 10, 30, 30))
        self.pushButtonA4 = QPushButton(self.centralwidget)
        self.pushButtonA4.setGeometry(QRect(100, 10, 30, 30))
        self.pushButtonA5 = QPushButton(self.centralwidget)
        self.pushButtonA5.setGeometry(QRect(130, 10, 30, 30))
        self.pushButtonA6 = QPushButton(self.centralwidget)
        self.pushButtonA6.setGeometry(QRect(160, 10, 30, 30))
        self.pushButtonA7 = QPushButton(self.centralwidget)
        self.pushButtonA7.setGeometry(QRect(190, 10, 30, 30))
        self.pushButtonA8 = QPushButton(self.centralwidget)
        self.pushButtonA8.setGeometry(QRect(220, 10, 30, 30))
        self.pushButtonA9 = QPushButton(self.centralwidget)
        self.pushButtonA9.setGeometry(QRect(250, 10, 30, 30))
        self.pushButtonA10 = QPushButton(self.centralwidget)
        self.pushButtonA10.setGeometry(QRect(280, 10, 30, 30))
        self.pushButtonA11 = QPushButton(self.centralwidget)
        self.pushButtonA11.setGeometry(QRect(310, 10, 30, 30))
        self.pushButtonA12 = QPushButton(self.centralwidget)
        self.pushButtonA12.setGeometry(QRect(340, 10, 30, 30))
        self.pushButtonA13 = QPushButton(self.centralwidget)
        self.pushButtonA13.setGeometry(QRect(370, 10, 30, 30))
        self.pushButtonA14 = QPushButton(self.centralwidget)
        self.pushButtonA14.setGeometry(QRect(400, 10, 30, 30))
        self.pushButtonA15 = QPushButton(self.centralwidget)
        self.pushButtonA15.setGeometry(QRect(430, 10, 30, 30))
        # Second line
        self.pushButtonB1 = QPushButton(self.centralwidget)
        self.pushButtonB1.setGeometry(QRect(10, 40, 30, 30))
        self.pushButtonB2 = QPushButton(self.centralwidget)
        self.pushButtonB2.setGeometry(QRect(40, 40, 30, 30))
        self.pushButtonB3 = QPushButton(self.centralwidget)
        self.pushButtonB3.setGeometry(QRect(70, 40, 30, 30))
        self.pushButtonB4 = QPushButton(self.centralwidget)
        self.pushButtonB4.setGeometry(QRect(100, 40, 30, 30))
        self.pushButtonB5 = QPushButton(self.centralwidget)
        self.pushButtonB5.setGeometry(QRect(130, 40, 30, 30))
        self.pushButtonB6 = QPushButton(self.centralwidget)
        self.pushButtonB6.setGeometry(QRect(160, 40, 30, 30))
        self.pushButtonB7 = QPushButton(self.centralwidget)
        self.pushButtonB7.setGeometry(QRect(190, 40, 30, 30))
        self.pushButtonB8 = QPushButton(self.centralwidget)
        self.pushButtonB8.setGeometry(QRect(220, 40, 30, 30))
        self.pushButtonB9 = QPushButton(self.centralwidget)
        self.pushButtonB9.setGeometry(QRect(250, 40, 30, 30))
        self.pushButtonB10 = QPushButton(self.centralwidget)
        self.pushButtonB10.setGeometry(QRect(280, 40, 30, 30))
        self.pushButtonB11 = QPushButton(self.centralwidget)
        self.pushButtonB11.setGeometry(QRect(310, 40, 30, 30))
        self.pushButtonB12 = QPushButton(self.centralwidget)
        self.pushButtonB12.setGeometry(QRect(340, 40, 30, 30))
        self.pushButtonB13 = QPushButton(self.centralwidget)
        self.pushButtonB13.setGeometry(QRect(370, 40, 30, 30))
        self.pushButtonB14 = QPushButton(self.centralwidget)
        self.pushButtonB14.setGeometry(QRect(400, 40, 30, 30))
        self.pushButtonB15 = QPushButton(self.centralwidget)
        self.pushButtonB15.setGeometry(QRect(430, 40, 30, 30))
        # Third line
        self.pushButtonC1 = QPushButton(self.centralwidget)
        self.pushButtonC1.setGeometry(QRect(10, 70, 30, 30))
        self.pushButtonC2 = QPushButton(self.centralwidget)
        self.pushButtonC2.setGeometry(QRect(40, 70, 30, 30))
        self.pushButtonC3 = QPushButton(self.centralwidget)
        self.pushButtonC3.setGeometry(QRect(70, 70, 30, 30))
        self.pushButtonC4 = QPushButton(self.centralwidget)
        self.pushButtonC4.setGeometry(QRect(100, 70, 30, 30))
        self.pushButtonC5 = QPushButton(self.centralwidget)
        self.pushButtonC5.setGeometry(QRect(130, 70, 30, 30))
        self.pushButtonC6 = QPushButton(self.centralwidget)
        self.pushButtonC6.setGeometry(QRect(160, 70, 30, 30))
        self.pushButtonC7 = QPushButton(self.centralwidget)
        self.pushButtonC7.setGeometry(QRect(190, 70, 30, 30))
        self.pushButtonC8 = QPushButton(self.centralwidget)
        self.pushButtonC8.setGeometry(QRect(220, 70, 30, 30))
        self.pushButtonC9 = QPushButton(self.centralwidget)
        self.pushButtonC9.setGeometry(QRect(250, 70, 30, 30))
        self.pushButtonC10 = QPushButton(self.centralwidget)
        self.pushButtonC10.setGeometry(QRect(280, 70, 30, 30))
        self.pushButtonC11 = QPushButton(self.centralwidget)
        self.pushButtonC11.setGeometry(QRect(310, 70, 30, 30))
        self.pushButtonC12 = QPushButton(self.centralwidget)
        self.pushButtonC12.setGeometry(QRect(340, 70, 30, 30))
        self.pushButtonC13 = QPushButton(self.centralwidget)
        self.pushButtonC13.setGeometry(QRect(370, 70, 30, 30))
        self.pushButtonC14 = QPushButton(self.centralwidget)
        self.pushButtonC14.setGeometry(QRect(400, 70, 30, 30))
        self.pushButtonC15 = QPushButton(self.centralwidget)
        self.pushButtonC15.setGeometry(QRect(430, 70, 30, 30))
        # Fourth line
        self.pushButtonD1 = QPushButton(self.centralwidget)
        self.pushButtonD1.setGeometry(QRect(10, 100, 30, 30))
        self.pushButtonD2 = QPushButton(self.centralwidget)
        self.pushButtonD2.setGeometry(QRect(40, 100, 30, 30))
        self.pushButtonD3 = QPushButton(self.centralwidget)
        self.pushButtonD3.setGeometry(QRect(70, 100, 30, 30))
        self.pushButtonD4 = QPushButton(self.centralwidget)
        self.pushButtonD4.setGeometry(QRect(100, 100, 30, 30))
        self.pushButtonD5 = QPushButton(self.centralwidget)
        self.pushButtonD5.setGeometry(QRect(130, 100, 30, 30))
        self.pushButtonD6 = QPushButton(self.centralwidget)
        self.pushButtonD6.setGeometry(QRect(160, 100, 30, 30))
        self.pushButtonD7 = QPushButton(self.centralwidget)
        self.pushButtonD7.setGeometry(QRect(190, 100, 30, 30))
        self.pushButtonD8 = QPushButton(self.centralwidget)
        self.pushButtonD8.setGeometry(QRect(220, 100, 30, 30))
        self.pushButtonD9 = QPushButton(self.centralwidget)
        self.pushButtonD9.setGeometry(QRect(250, 100, 30, 30))
        self.pushButtonD10 = QPushButton(self.centralwidget)
        self.pushButtonD10.setGeometry(QRect(280, 100, 30, 30))
        self.pushButtonD11 = QPushButton(self.centralwidget)
        self.pushButtonD11.setGeometry(QRect(310, 100, 30, 30))
        self.pushButtonD12 = QPushButton(self.centralwidget)
        self.pushButtonD12.setGeometry(QRect(340, 100, 30, 30))
        self.pushButtonD13 = QPushButton(self.centralwidget)
        self.pushButtonD13.setGeometry(QRect(370, 100, 30, 30))
        self.pushButtonD14 = QPushButton(self.centralwidget)
        self.pushButtonD14.setGeometry(QRect(400, 100, 30, 30))
        self.pushButtonD15 = QPushButton(self.centralwidget)
        self.pushButtonD15.setGeometry(QRect(430, 100, 30, 30))
        # Fiveth line
        self.pushButtonE1 = QPushButton(self.centralwidget)
        self.pushButtonE1.setGeometry(QRect(10, 130, 30, 30))
        self.pushButtonE2 = QPushButton(self.centralwidget)
        self.pushButtonE2.setGeometry(QRect(40, 130, 30, 30))
        self.pushButtonE3 = QPushButton(self.centralwidget)
        self.pushButtonE3.setGeometry(QRect(70, 130, 30, 30))
        self.pushButtonE4 = QPushButton(self.centralwidget)
        self.pushButtonE4.setGeometry(QRect(100, 130, 30, 30))
        self.pushButtonE5 = QPushButton(self.centralwidget)
        self.pushButtonE5.setGeometry(QRect(130, 130, 30, 30))
        self.pushButtonE6 = QPushButton(self.centralwidget)
        self.pushButtonE6.setGeometry(QRect(160, 130, 30, 30))
        self.pushButtonE7 = QPushButton(self.centralwidget)
        self.pushButtonE7.setGeometry(QRect(190, 130, 30, 30))
        self.pushButtonE8 = QPushButton(self.centralwidget)
        self.pushButtonE8.setGeometry(QRect(220, 130, 30, 30))
        self.pushButtonE9 = QPushButton(self.centralwidget)
        self.pushButtonE9.setGeometry(QRect(250, 130, 30, 30))
        self.pushButtonE10 = QPushButton(self.centralwidget)
        self.pushButtonE10.setGeometry(QRect(280, 130, 30, 30))
        self.pushButtonE11 = QPushButton(self.centralwidget)
        self.pushButtonE11.setGeometry(QRect(310, 130, 30, 30))
        self.pushButtonE12 = QPushButton(self.centralwidget)
        self.pushButtonE12.setGeometry(QRect(340, 130, 30, 30))
        self.pushButtonE13 = QPushButton(self.centralwidget)
        self.pushButtonE13.setGeometry(QRect(370, 130, 30, 30))
        self.pushButtonE14 = QPushButton(self.centralwidget)
        self.pushButtonE14.setGeometry(QRect(400, 130, 30, 30))
        self.pushButtonE15 = QPushButton(self.centralwidget)
        self.pushButtonE15.setGeometry(QRect(430, 130, 30, 30))
        # Sixth line
        self.pushButtonF1 = QPushButton(self.centralwidget)
        self.pushButtonF1.setGeometry(QRect(10, 160, 30, 30))
        self.pushButtonF2 = QPushButton(self.centralwidget)
        self.pushButtonF2.setGeometry(QRect(40, 160, 30, 30))
        self.pushButtonF3 = QPushButton(self.centralwidget)
        self.pushButtonF3.setGeometry(QRect(70, 160, 30, 30))
        self.pushButtonF4 = QPushButton(self.centralwidget)
        self.pushButtonF4.setGeometry(QRect(100, 160, 30, 30))
        self.pushButtonF5 = QPushButton(self.centralwidget)
        self.pushButtonF5.setGeometry(QRect(130, 160, 30, 30))
        self.pushButtonF6 = QPushButton(self.centralwidget)
        self.pushButtonF6.setGeometry(QRect(160, 160, 30, 30))
        self.pushButtonF7 = QPushButton(self.centralwidget)
        self.pushButtonF7.setGeometry(QRect(190, 160, 30, 30))
        self.pushButtonF8 = QPushButton(self.centralwidget)
        self.pushButtonF8.setGeometry(QRect(220, 160, 30, 30))
        self.pushButtonF9 = QPushButton(self.centralwidget)
        self.pushButtonF9.setGeometry(QRect(250, 160, 30, 30))
        self.pushButtonF10 = QPushButton(self.centralwidget)
        self.pushButtonF10.setGeometry(QRect(280, 160, 30, 30))
        self.pushButtonF11 = QPushButton(self.centralwidget)
        self.pushButtonF11.setGeometry(QRect(310, 160, 30, 30))
        self.pushButtonF12 = QPushButton(self.centralwidget)
        self.pushButtonF12.setGeometry(QRect(340, 160, 30, 30))
        self.pushButtonF13 = QPushButton(self.centralwidget)
        self.pushButtonF13.setGeometry(QRect(370, 160, 30, 30))
        self.pushButtonF14 = QPushButton(self.centralwidget)
        self.pushButtonF14.setGeometry(QRect(400, 160, 30, 30))
        self.pushButtonF15 = QPushButton(self.centralwidget)
        self.pushButtonF15.setGeometry(QRect(430, 160, 30, 30))
        # Seventh line
        self.pushButtonG1 = QPushButton(self.centralwidget)
        self.pushButtonG1.setGeometry(QRect(10, 190, 30, 30))
        self.pushButtonG2 = QPushButton(self.centralwidget)
        self.pushButtonG2.setGeometry(QRect(40, 190, 30, 30))
        self.pushButtonG3 = QPushButton(self.centralwidget)
        self.pushButtonG3.setGeometry(QRect(70, 190, 30, 30))
        self.pushButtonG4 = QPushButton(self.centralwidget)
        self.pushButtonG4.setGeometry(QRect(100, 190, 30, 30))
        self.pushButtonG5 = QPushButton(self.centralwidget)
        self.pushButtonG5.setGeometry(QRect(130, 190, 30, 30))
        self.pushButtonG6 = QPushButton(self.centralwidget)
        self.pushButtonG6.setGeometry(QRect(160, 190, 30, 30))
        self.pushButtonG7 = QPushButton(self.centralwidget)
        self.pushButtonG7.setGeometry(QRect(190, 190, 30, 30))
        self.pushButtonG8 = QPushButton(self.centralwidget)
        self.pushButtonG8.setGeometry(QRect(220, 190, 30, 30))
        self.pushButtonG9 = QPushButton(self.centralwidget)
        self.pushButtonG9.setGeometry(QRect(250, 190, 30, 30))
        self.pushButtonG10 = QPushButton(self.centralwidget)
        self.pushButtonG10.setGeometry(QRect(280, 190, 30, 30))
        self.pushButtonG11 = QPushButton(self.centralwidget)
        self.pushButtonG11.setGeometry(QRect(310, 190, 30, 30))
        self.pushButtonG12 = QPushButton(self.centralwidget)
        self.pushButtonG12.setGeometry(QRect(340, 190, 30, 30))
        self.pushButtonG13 = QPushButton(self.centralwidget)
        self.pushButtonG13.setGeometry(QRect(370, 190, 30, 30))
        self.pushButtonG14 = QPushButton(self.centralwidget)
        self.pushButtonG14.setGeometry(QRect(400, 190, 30, 30))
        self.pushButtonG15 = QPushButton(self.centralwidget)
        self.pushButtonG15.setGeometry(QRect(430, 190, 30, 30))
        # Eighth line
        self.pushButtonH1 = QPushButton(self.centralwidget)
        self.pushButtonH1.setGeometry(QRect(10, 220, 30, 30))
        self.pushButtonH2 = QPushButton(self.centralwidget)
        self.pushButtonH2.setGeometry(QRect(40, 220, 30, 30))
        self.pushButtonH3 = QPushButton(self.centralwidget)
        self.pushButtonH3.setGeometry(QRect(70, 220, 30, 30))
        self.pushButtonH4 = QPushButton(self.centralwidget)
        self.pushButtonH4.setGeometry(QRect(100, 220, 30, 30))
        self.pushButtonH5 = QPushButton(self.centralwidget)
        self.pushButtonH5.setGeometry(QRect(130, 220, 30, 30))
        self.pushButtonH6 = QPushButton(self.centralwidget)
        self.pushButtonH6.setGeometry(QRect(160, 220, 30, 30))
        self.pushButtonH7 = QPushButton(self.centralwidget)
        self.pushButtonH7.setGeometry(QRect(190, 220, 30, 30))
        self.pushButtonH8 = QPushButton(self.centralwidget)
        self.pushButtonH8.setGeometry(QRect(220, 220, 30, 30))
        self.pushButtonH9 = QPushButton(self.centralwidget)
        self.pushButtonH9.setGeometry(QRect(250, 220, 30, 30))
        self.pushButtonH10 = QPushButton(self.centralwidget)
        self.pushButtonH10.setGeometry(QRect(280, 220, 30, 30))
        self.pushButtonH11 = QPushButton(self.centralwidget)
        self.pushButtonH11.setGeometry(QRect(310, 220, 30, 30))
        self.pushButtonH12 = QPushButton(self.centralwidget)
        self.pushButtonH12.setGeometry(QRect(340, 220, 30, 30))
        self.pushButtonH13 = QPushButton(self.centralwidget)
        self.pushButtonH13.setGeometry(QRect(370, 220, 30, 30))
        self.pushButtonH14 = QPushButton(self.centralwidget)
        self.pushButtonH14.setGeometry(QRect(400, 220, 30, 30))
        self.pushButtonH15 = QPushButton(self.centralwidget)
        self.pushButtonH15.setGeometry(QRect(430, 220, 30, 30))
        # Nineth line
        self.pushButtonI1 = QPushButton(self.centralwidget)
        self.pushButtonI1.setGeometry(QRect(10, 250, 30, 30))
        self.pushButtonI2 = QPushButton(self.centralwidget)
        self.pushButtonI2.setGeometry(QRect(40, 250, 30, 30))
        self.pushButtonI3 = QPushButton(self.centralwidget)
        self.pushButtonI3.setGeometry(QRect(70, 250, 30, 30))
        self.pushButtonI4 = QPushButton(self.centralwidget)
        self.pushButtonI4.setGeometry(QRect(100, 250, 30, 30))
        self.pushButtonI5 = QPushButton(self.centralwidget)
        self.pushButtonI5.setGeometry(QRect(130, 250, 30, 30))
        self.pushButtonI6 = QPushButton(self.centralwidget)
        self.pushButtonI6.setGeometry(QRect(160, 250, 30, 30))
        self.pushButtonI7 = QPushButton(self.centralwidget)
        self.pushButtonI7.setGeometry(QRect(190, 250, 30, 30))
        self.pushButtonI8 = QPushButton(self.centralwidget)
        self.pushButtonI8.setGeometry(QRect(220, 250, 30, 30))
        self.pushButtonI9 = QPushButton(self.centralwidget)
        self.pushButtonI9.setGeometry(QRect(250, 250, 30, 30))
        self.pushButtonI10 = QPushButton(self.centralwidget)
        self.pushButtonI10.setGeometry(QRect(280, 250, 30, 30))
        self.pushButtonI11 = QPushButton(self.centralwidget)
        self.pushButtonI11.setGeometry(QRect(310, 250, 30, 30))
        self.pushButtonI12 = QPushButton(self.centralwidget)
        self.pushButtonI12.setGeometry(QRect(340, 250, 30, 30))
        self.pushButtonI13 = QPushButton(self.centralwidget)
        self.pushButtonI13.setGeometry(QRect(370, 250, 30, 30))
        self.pushButtonI14 = QPushButton(self.centralwidget)
        self.pushButtonI14.setGeometry(QRect(400, 250, 30, 30))
        self.pushButtonI15 = QPushButton(self.centralwidget)
        self.pushButtonI15.setGeometry(QRect(430, 250, 30, 30))
        # Tenth line
        self.pushButtonJ1 = QPushButton(self.centralwidget)
        self.pushButtonJ1.setGeometry(QRect(10, 280, 30, 30))
        self.pushButtonJ2 = QPushButton(self.centralwidget)
        self.pushButtonJ2.setGeometry(QRect(40, 280, 30, 30))
        self.pushButtonJ3 = QPushButton(self.centralwidget)
        self.pushButtonJ3.setGeometry(QRect(70, 280, 30, 30))
        self.pushButtonJ4 = QPushButton(self.centralwidget)
        self.pushButtonJ4.setGeometry(QRect(100, 280, 30, 30))
        self.pushButtonJ5 = QPushButton(self.centralwidget)
        self.pushButtonJ5.setGeometry(QRect(130, 280, 30, 30))
        self.pushButtonJ6 = QPushButton(self.centralwidget)
        self.pushButtonJ6.setGeometry(QRect(160, 280, 30, 30))
        self.pushButtonJ7 = QPushButton(self.centralwidget)
        self.pushButtonJ7.setGeometry(QRect(190, 280, 30, 30))
        self.pushButtonJ8 = QPushButton(self.centralwidget)
        self.pushButtonJ8.setGeometry(QRect(220, 280, 30, 30))
        self.pushButtonJ9 = QPushButton(self.centralwidget)
        self.pushButtonJ9.setGeometry(QRect(250, 280, 30, 30))
        self.pushButtonJ10 = QPushButton(self.centralwidget)
        self.pushButtonJ10.setGeometry(QRect(280, 280, 30, 30))
        self.pushButtonJ11 = QPushButton(self.centralwidget)
        self.pushButtonJ11.setGeometry(QRect(310, 280, 30, 30))
        self.pushButtonJ12 = QPushButton(self.centralwidget)
        self.pushButtonJ12.setGeometry(QRect(340, 280, 30, 30))
        self.pushButtonJ13 = QPushButton(self.centralwidget)
        self.pushButtonJ13.setGeometry(QRect(370, 280, 30, 30))
        self.pushButtonJ14 = QPushButton(self.centralwidget)
        self.pushButtonJ14.setGeometry(QRect(400, 280, 30, 30))
        self.pushButtonJ15 = QPushButton(self.centralwidget)
        self.pushButtonJ15.setGeometry(QRect(430, 280, 30, 30))
        # Eleventh line
        self.pushButtonK1 = QPushButton(self.centralwidget)
        self.pushButtonK1.setGeometry(QRect(10, 310, 30, 30))
        self.pushButtonK2 = QPushButton(self.centralwidget)
        self.pushButtonK2.setGeometry(QRect(40, 310, 30, 30))
        self.pushButtonK3 = QPushButton(self.centralwidget)
        self.pushButtonK3.setGeometry(QRect(70, 310, 30, 30))
        self.pushButtonK4 = QPushButton(self.centralwidget)
        self.pushButtonK4.setGeometry(QRect(100, 310, 30, 30))
        self.pushButtonK5 = QPushButton(self.centralwidget)
        self.pushButtonK5.setGeometry(QRect(130, 310, 30, 30))
        self.pushButtonK6 = QPushButton(self.centralwidget)
        self.pushButtonK6.setGeometry(QRect(160, 310, 30, 30))
        self.pushButtonK7 = QPushButton(self.centralwidget)
        self.pushButtonK7.setGeometry(QRect(190, 310, 30, 30))
        self.pushButtonK8 = QPushButton(self.centralwidget)
        self.pushButtonK8.setGeometry(QRect(220, 310, 30, 30))
        self.pushButtonK9 = QPushButton(self.centralwidget)
        self.pushButtonK9.setGeometry(QRect(250, 310, 30, 30))
        self.pushButtonK10 = QPushButton(self.centralwidget)
        self.pushButtonK10.setGeometry(QRect(280, 310, 30, 30))
        self.pushButtonK11 = QPushButton(self.centralwidget)
        self.pushButtonK11.setGeometry(QRect(310, 310, 30, 30))
        self.pushButtonK12 = QPushButton(self.centralwidget)
        self.pushButtonK12.setGeometry(QRect(340, 310, 30, 30))
        self.pushButtonK13 = QPushButton(self.centralwidget)
        self.pushButtonK13.setGeometry(QRect(370, 310, 30, 30))
        self.pushButtonK14 = QPushButton(self.centralwidget)
        self.pushButtonK14.setGeometry(QRect(400, 310, 30, 30))
        self.pushButtonK15 = QPushButton(self.centralwidget)
        self.pushButtonK15.setGeometry(QRect(430, 310, 30, 30))
        # Twelveth line
        self.pushButtonL1 = QPushButton(self.centralwidget)
        self.pushButtonL1.setGeometry(QRect(10, 340, 30, 30))
        self.pushButtonL2 = QPushButton(self.centralwidget)
        self.pushButtonL2.setGeometry(QRect(40, 340, 30, 30))
        self.pushButtonL3 = QPushButton(self.centralwidget)
        self.pushButtonL3.setGeometry(QRect(70, 340, 30, 30))
        self.pushButtonL4 = QPushButton(self.centralwidget)
        self.pushButtonL4.setGeometry(QRect(100, 340, 30, 30))
        self.pushButtonL5 = QPushButton(self.centralwidget)
        self.pushButtonL5.setGeometry(QRect(130, 340, 30, 30))
        self.pushButtonL6 = QPushButton(self.centralwidget)
        self.pushButtonL6.setGeometry(QRect(160, 340, 30, 30))
        self.pushButtonL7 = QPushButton(self.centralwidget)
        self.pushButtonL7.setGeometry(QRect(190, 340, 30, 30))
        self.pushButtonL8 = QPushButton(self.centralwidget)
        self.pushButtonL8.setGeometry(QRect(220, 340, 30, 30))
        self.pushButtonL9 = QPushButton(self.centralwidget)
        self.pushButtonL9.setGeometry(QRect(250, 340, 30, 30))
        self.pushButtonL10 = QPushButton(self.centralwidget)
        self.pushButtonL10.setGeometry(QRect(280, 340, 30, 30))
        self.pushButtonL11 = QPushButton(self.centralwidget)
        self.pushButtonL11.setGeometry(QRect(310, 340, 30, 30))
        self.pushButtonL12 = QPushButton(self.centralwidget)
        self.pushButtonL12.setGeometry(QRect(340, 340, 30, 30))
        self.pushButtonL13 = QPushButton(self.centralwidget)
        self.pushButtonL13.setGeometry(QRect(370, 340, 30, 30))
        self.pushButtonL14 = QPushButton(self.centralwidget)
        self.pushButtonL14.setGeometry(QRect(400, 340, 30, 30))
        self.pushButtonL15 = QPushButton(self.centralwidget)
        self.pushButtonL15.setGeometry(QRect(430, 340, 30, 30))
        # Thirteenth line
        self.pushButtonM1 = QPushButton(self.centralwidget)
        self.pushButtonM1.setGeometry(QRect(10, 370, 30, 30))
        self.pushButtonM2 = QPushButton(self.centralwidget)
        self.pushButtonM2.setGeometry(QRect(40, 370, 30, 30))
        self.pushButtonM3 = QPushButton(self.centralwidget)
        self.pushButtonM3.setGeometry(QRect(70, 370, 30, 30))
        self.pushButtonM4 = QPushButton(self.centralwidget)
        self.pushButtonM4.setGeometry(QRect(100, 370, 30, 30))
        self.pushButtonM5 = QPushButton(self.centralwidget)
        self.pushButtonM5.setGeometry(QRect(130, 370, 30, 30))
        self.pushButtonM6 = QPushButton(self.centralwidget)
        self.pushButtonM6.setGeometry(QRect(160, 370, 30, 30))
        self.pushButtonM7 = QPushButton(self.centralwidget)
        self.pushButtonM7.setGeometry(QRect(190, 370, 30, 30))
        self.pushButtonM8 = QPushButton(self.centralwidget)
        self.pushButtonM8.setGeometry(QRect(220, 370, 30, 30))
        self.pushButtonM9 = QPushButton(self.centralwidget)
        self.pushButtonM9.setGeometry(QRect(250, 370, 30, 30))
        self.pushButtonM10 = QPushButton(self.centralwidget)
        self.pushButtonM10.setGeometry(QRect(280, 370, 30, 30))
        self.pushButtonM11 = QPushButton(self.centralwidget)
        self.pushButtonM11.setGeometry(QRect(310, 370, 30, 30))
        self.pushButtonM12 = QPushButton(self.centralwidget)
        self.pushButtonM12.setGeometry(QRect(340, 370, 30, 30))
        self.pushButtonM13 = QPushButton(self.centralwidget)
        self.pushButtonM13.setGeometry(QRect(370, 370, 30, 30))
        self.pushButtonM14 = QPushButton(self.centralwidget)
        self.pushButtonM14.setGeometry(QRect(400, 370, 30, 30))
        self.pushButtonM15 = QPushButton(self.centralwidget)
        self.pushButtonM15.setGeometry(QRect(430, 370, 30, 30))
        # Fourteenth line
        self.pushButtonN1 = QPushButton(self.centralwidget)
        self.pushButtonN1.setGeometry(QRect(10, 400, 30, 30))
        self.pushButtonN2 = QPushButton(self.centralwidget)
        self.pushButtonN2.setGeometry(QRect(40, 400, 30, 30))
        self.pushButtonN3 = QPushButton(self.centralwidget)
        self.pushButtonN3.setGeometry(QRect(70, 400, 30, 30))
        self.pushButtonN4 = QPushButton(self.centralwidget)
        self.pushButtonN4.setGeometry(QRect(100, 400, 30, 30))
        self.pushButtonN5 = QPushButton(self.centralwidget)
        self.pushButtonN5.setGeometry(QRect(130, 400, 30, 30))
        self.pushButtonN6 = QPushButton(self.centralwidget)
        self.pushButtonN6.setGeometry(QRect(160, 400, 30, 30))
        self.pushButtonN7 = QPushButton(self.centralwidget)
        self.pushButtonN7.setGeometry(QRect(190, 400, 30, 30))
        self.pushButtonN8 = QPushButton(self.centralwidget)
        self.pushButtonN8.setGeometry(QRect(220, 400, 30, 30))
        self.pushButtonN9 = QPushButton(self.centralwidget)
        self.pushButtonN9.setGeometry(QRect(250, 400, 30, 30))
        self.pushButtonN10 = QPushButton(self.centralwidget)
        self.pushButtonN10.setGeometry(QRect(280, 400, 30, 30))
        self.pushButtonN11 = QPushButton(self.centralwidget)
        self.pushButtonN11.setGeometry(QRect(310, 400, 30, 30))
        self.pushButtonN12 = QPushButton(self.centralwidget)
        self.pushButtonN12.setGeometry(QRect(340, 400, 30, 30))
        self.pushButtonN13 = QPushButton(self.centralwidget)
        self.pushButtonN13.setGeometry(QRect(370, 400, 30, 30))
        self.pushButtonN14 = QPushButton(self.centralwidget)
        self.pushButtonN14.setGeometry(QRect(400, 400, 30, 30))
        self.pushButtonN15 = QPushButton(self.centralwidget)
        self.pushButtonN15.setGeometry(QRect(430, 400, 30, 30))
        # Fiveteenth line
        self.pushButtonO1 = QPushButton(self.centralwidget)
        self.pushButtonO1.setGeometry(QRect(10, 430, 30, 30))
        self.pushButtonO2 = QPushButton(self.centralwidget)
        self.pushButtonO2.setGeometry(QRect(40, 430, 30, 30))
        self.pushButtonO3 = QPushButton(self.centralwidget)
        self.pushButtonO3.setGeometry(QRect(70, 430, 30, 30))
        self.pushButtonO4 = QPushButton(self.centralwidget)
        self.pushButtonO4.setGeometry(QRect(100, 430, 30, 30))
        self.pushButtonO5 = QPushButton(self.centralwidget)
        self.pushButtonO5.setGeometry(QRect(130, 430, 30, 30))
        self.pushButtonO6 = QPushButton(self.centralwidget)
        self.pushButtonO6.setGeometry(QRect(160, 430, 30, 30))
        self.pushButtonO7 = QPushButton(self.centralwidget)
        self.pushButtonO7.setGeometry(QRect(190, 430, 30, 30))
        self.pushButtonO8 = QPushButton(self.centralwidget)
        self.pushButtonO8.setGeometry(QRect(220, 430, 30, 30))
        self.pushButtonO9 = QPushButton(self.centralwidget)
        self.pushButtonO9.setGeometry(QRect(250, 430, 30, 30))
        self.pushButtonO10 = QPushButton(self.centralwidget)
        self.pushButtonO10.setGeometry(QRect(280, 430, 30, 30))
        self.pushButtonO11 = QPushButton(self.centralwidget)
        self.pushButtonO11.setGeometry(QRect(310, 430, 30, 30))
        self.pushButtonO12 = QPushButton(self.centralwidget)
        self.pushButtonO12.setGeometry(QRect(340, 430, 30, 30))
        self.pushButtonO13 = QPushButton(self.centralwidget)
        self.pushButtonO13.setGeometry(QRect(370, 430, 30, 30))
        self.pushButtonO14 = QPushButton(self.centralwidget)
        self.pushButtonO14.setGeometry(QRect(400, 430, 30, 30))
        self.pushButtonO15 = QPushButton(self.centralwidget)
        self.pushButtonO15.setGeometry(QRect(430, 430, 30, 30))
        # Button flag
        self.pushButtonFlag = QPushButton(self.centralwidget)
        self.pushButtonFlag.setGeometry(QRect(50, 480, 30, 30))
        self.pushButtonFlag.clicked.connect(self.toggle_flag_status)
        self.pushButtonFlag.setIcon(self.icons.get_icon_flag())
        self.pushButtonFlag.setIconSize(QSize(28, 28))
        # Create timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timer_event)
        self.timer_label = QLabel(self.centralwidget)
        self.timer_label.setGeometry(QRect(200, 510, 81, 16))
        self.timer_label_2 = QLabel(self.centralwidget)
        self.timer_label_2.setGeometry(QRect(205, 490, 81, 16))
        self.timer_label_2.setText("Timer")
        # Create flag label
        self.flag_label = QLabel(self.centralwidget)
        self.flag_label.setGeometry(QRect(45, 510, 81, 16))
        # Create central widget
        MainWindow.setCentralWidget(self.centralwidget)
        # Create board
        self.create_board()
        # Create button fucntions
        self.create_button_functions()
        # Create flag label
        self.bombs_label = QLabel(self.centralwidget)
        self.bombs_label.setGeometry(QRect(370, 510, 81, 16))
        self.bombs_label_2 = QLabel(self.centralwidget)
        self.bombs_label_2.setGeometry(QRect(350, 490, 81, 16))
        self.bombs_label_2.setText("Bombs quantity")
        self.init_game_configs()

    def erase_board(self):
        for i in range(Ui_MainWindow.LENGTH_AXIS_Y):
            for j in range(Ui_MainWindow.LENGTH_AXIS_X):
                self.board[i][j].value = '0'
                icon = self.show_image('g')
                self.board[i][j].setIcon(icon)
                self.board[i][j].setIconSize(QSize(28, 28))
                self.board[i][j].is_flag = False
                self.board[i][j].setCheckable(True)

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
                if self.board[j][i].isCheckable():
                    self.function_click_buttons[j][i]()

    def click_pushButtonA1(self):
        self.process_button(0, 0)

    def click_pushButtonA2(self):
        self.process_button(1, 0)

    def click_pushButtonA3(self):
        self.process_button(2, 0)

    def click_pushButtonA4(self):
        self.process_button(3, 0)

    def click_pushButtonA5(self):
        self.process_button(4, 0)

    def click_pushButtonA6(self):
        self.process_button(5, 0)

    def click_pushButtonA7(self):
        self.process_button(6, 0)

    def click_pushButtonA8(self):
        self.process_button(7, 0)

    def click_pushButtonA9(self):
        self.process_button(8, 0)

    def click_pushButtonA10(self):
        self.process_button(9, 0)

    def click_pushButtonA11(self):
        self.process_button(10, 0)

    def click_pushButtonA12(self):
        self.process_button(11, 0)

    def click_pushButtonA13(self):
        self.process_button(12, 0)

    def click_pushButtonA14(self):
        self.process_button(13, 0)

    def click_pushButtonA15(self):
        self.process_button(14, 0)

    def click_pushButtonB1(self):
        self.process_button(0, 1)

    def click_pushButtonB2(self):
        self.process_button(1, 1)

    def click_pushButtonB3(self):
        self.process_button(2, 1)

    def click_pushButtonB4(self):
        self.process_button(3, 1)

    def click_pushButtonB5(self):
        self.process_button(4, 1)

    def click_pushButtonB6(self):
        self.process_button(5, 1)

    def click_pushButtonB7(self):
        self.process_button(6, 1)

    def click_pushButtonB8(self):
        self.process_button(7, 1)

    def click_pushButtonB9(self):
        self.process_button(8, 1)

    def click_pushButtonB10(self):
        self.process_button(9, 1)

    def click_pushButtonB11(self):
        self.process_button(10, 1)

    def click_pushButtonB12(self):
        self.process_button(11, 1)

    def click_pushButtonB13(self):
        self.process_button(12, 1)

    def click_pushButtonB14(self):
        self.process_button(13, 1)

    def click_pushButtonB15(self):
        self.process_button(14, 1)

    def click_pushButtonC1(self):
        self.process_button(0, 2)

    def click_pushButtonC2(self):
        self.process_button(1, 2)

    def click_pushButtonC3(self):
        self.process_button(2, 2)

    def click_pushButtonC4(self):
        self.process_button(3, 2)

    def click_pushButtonC5(self):
        self.process_button(4, 2)

    def click_pushButtonC6(self):
        self.process_button(5, 2)

    def click_pushButtonC7(self):
        self.process_button(6, 2)

    def click_pushButtonC8(self):
        self.process_button(7, 2)

    def click_pushButtonC9(self):
        self.process_button(8, 2)

    def click_pushButtonC10(self):
        self.process_button(9, 2)

    def click_pushButtonC11(self):
        self.process_button(10, 2)

    def click_pushButtonC12(self):
        self.process_button(11, 2)

    def click_pushButtonC13(self):
        self.process_button(12, 2)

    def click_pushButtonC14(self):
        self.process_button(13, 2)

    def click_pushButtonC15(self):
        self.process_button(14, 2)

    def click_pushButtonD1(self):
        self.process_button(0, 3)

    def click_pushButtonD2(self):
        self.process_button(1, 3)

    def click_pushButtonD3(self):
        self.process_button(2, 3)

    def click_pushButtonD4(self):
        self.process_button(3, 3)

    def click_pushButtonD5(self):
        self.process_button(4, 3)

    def click_pushButtonD6(self):
        self.process_button(5, 3)

    def click_pushButtonD7(self):
        self.process_button(6, 3)

    def click_pushButtonD8(self):
        self.process_button(7, 3)

    def click_pushButtonD9(self):
        self.process_button(8, 3)

    def click_pushButtonD10(self):
        self.process_button(9, 3)

    def click_pushButtonD11(self):
        self.process_button(10, 3)

    def click_pushButtonD12(self):
        self.process_button(11, 3)

    def click_pushButtonD13(self):
        self.process_button(12, 3)

    def click_pushButtonD14(self):
        self.process_button(13, 3)

    def click_pushButtonD15(self):
        self.process_button(14, 3)

    def click_pushButtonE1(self):
        self.process_button(0, 4)

    def click_pushButtonE2(self):
        self.process_button(1, 4)

    def click_pushButtonE3(self):
        self.process_button(2, 4)

    def click_pushButtonE4(self):
        self.process_button(3, 4)

    def click_pushButtonE5(self):
        self.process_button(4, 4)

    def click_pushButtonE6(self):
        self.process_button(5, 4)

    def click_pushButtonE7(self):
        self.process_button(6, 4)

    def click_pushButtonE8(self):
        self.process_button(7, 4)

    def click_pushButtonE9(self):
        self.process_button(8, 4)

    def click_pushButtonE10(self):
        self.process_button(9, 4)

    def click_pushButtonE11(self):
        self.process_button(10, 4)

    def click_pushButtonE12(self):
        self.process_button(11, 4)

    def click_pushButtonE13(self):
        self.process_button(12, 4)

    def click_pushButtonE14(self):
        self.process_button(13, 4)

    def click_pushButtonE15(self):
        self.process_button(14, 4)

    def click_pushButtonF1(self):
        self.process_button(0, 5)

    def click_pushButtonF2(self):
        self.process_button(1, 5)

    def click_pushButtonF3(self):
        self.process_button(2, 5)

    def click_pushButtonF4(self):
        self.process_button(3, 5)

    def click_pushButtonF5(self):
        self.process_button(4, 5)

    def click_pushButtonF6(self):
        self.process_button(5, 5)

    def click_pushButtonF7(self):
        self.process_button(6, 5)

    def click_pushButtonF8(self):
        self.process_button(7, 5)

    def click_pushButtonF9(self):
        self.process_button(8, 5)

    def click_pushButtonF10(self):
        self.process_button(9, 5)

    def click_pushButtonF11(self):
        self.process_button(10, 5)

    def click_pushButtonF12(self):
        self.process_button(11, 5)

    def click_pushButtonF13(self):
        self.process_button(12, 5)

    def click_pushButtonF14(self):
        self.process_button(13, 5)

    def click_pushButtonF15(self):
        self.process_button(14, 5)

    def click_pushButtonG1(self):
        self.process_button(0, 6)

    def click_pushButtonG2(self):
        self.process_button(1, 6)

    def click_pushButtonG3(self):
        self.process_button(2, 6)

    def click_pushButtonG4(self):
        self.process_button(3, 6)

    def click_pushButtonG5(self):
        self.process_button(4, 6)

    def click_pushButtonG6(self):
        self.process_button(5, 6)

    def click_pushButtonG7(self):
        self.process_button(6, 6)

    def click_pushButtonG8(self):
        self.process_button(7, 6)

    def click_pushButtonG9(self):
        self.process_button(8, 6)

    def click_pushButtonG10(self):
        self.process_button(9, 6)

    def click_pushButtonG11(self):
        self.process_button(10, 6)

    def click_pushButtonG12(self):
        self.process_button(11, 6)

    def click_pushButtonG13(self):
        self.process_button(12, 6)

    def click_pushButtonG14(self):
        self.process_button(13, 6)

    def click_pushButtonG15(self):
        self.process_button(14, 6)

    def click_pushButtonH1(self):
        self.process_button(0, 7)

    def click_pushButtonH2(self):
        self.process_button(1, 7)

    def click_pushButtonH3(self):
        self.process_button(2, 7)

    def click_pushButtonH4(self):
        self.process_button(3, 7)

    def click_pushButtonH5(self):
        self.process_button(4, 7)

    def click_pushButtonH6(self):
        self.process_button(5, 7)

    def click_pushButtonH7(self):
        self.process_button(6, 7)

    def click_pushButtonH8(self):
        self.process_button(7, 7)

    def click_pushButtonH9(self):
        self.process_button(8, 7)

    def click_pushButtonH10(self):
        self.process_button(9, 7)

    def click_pushButtonH11(self):
        self.process_button(10, 7)

    def click_pushButtonH12(self):
        self.process_button(11, 7)

    def click_pushButtonH13(self):
        self.process_button(12, 7)

    def click_pushButtonH14(self):
        self.process_button(13, 7)

    def click_pushButtonH15(self):
        self.process_button(14, 7)

    def click_pushButtonI1(self):
        self.process_button(0, 8)

    def click_pushButtonI2(self):
        self.process_button(1, 8)

    def click_pushButtonI3(self):
        self.process_button(2, 8)

    def click_pushButtonI4(self):
        self.process_button(3, 8)

    def click_pushButtonI5(self):
        self.process_button(4, 8)

    def click_pushButtonI6(self):
        self.process_button(5, 8)

    def click_pushButtonI7(self):
        self.process_button(6, 8)

    def click_pushButtonI8(self):
        self.process_button(7, 8)

    def click_pushButtonI9(self):
        self.process_button(8, 8)

    def click_pushButtonI10(self):
        self.process_button(9, 8)

    def click_pushButtonI11(self):
        self.process_button(10, 8)

    def click_pushButtonI12(self):
        self.process_button(11, 8)

    def click_pushButtonI13(self):
        self.process_button(12, 8)

    def click_pushButtonI14(self):
        self.process_button(13, 8)

    def click_pushButtonI15(self):
        self.process_button(14, 8)

    def click_pushButtonJ1(self):
        self.process_button(0, 9)

    def click_pushButtonJ2(self):
        self.process_button(1, 9)

    def click_pushButtonJ3(self):
        self.process_button(2, 9)

    def click_pushButtonJ4(self):
        self.process_button(3, 9)

    def click_pushButtonJ5(self):
        self.process_button(4, 9)

    def click_pushButtonJ6(self):
        self.process_button(5, 9)

    def click_pushButtonJ7(self):
        self.process_button(6, 9)

    def click_pushButtonJ8(self):
        self.process_button(7, 9)

    def click_pushButtonJ9(self):
        self.process_button(8, 9)

    def click_pushButtonJ10(self):
        self.process_button(9, 9)

    def click_pushButtonJ11(self):
        self.process_button(10, 9)

    def click_pushButtonJ12(self):
        self.process_button(11, 9)

    def click_pushButtonJ13(self):
        self.process_button(12, 9)

    def click_pushButtonJ14(self):
        self.process_button(13, 9)

    def click_pushButtonJ15(self):
        self.process_button(14, 9)

    def click_pushButtonK1(self):
        self.process_button(0, 10)

    def click_pushButtonK2(self):
        self.process_button(1, 10)

    def click_pushButtonK3(self):
        self.process_button(2, 10)

    def click_pushButtonK4(self):
        self.process_button(3, 10)

    def click_pushButtonK5(self):
        self.process_button(4, 10)

    def click_pushButtonK6(self):
        self.process_button(5, 10)

    def click_pushButtonK7(self):
        self.process_button(6, 10)

    def click_pushButtonK8(self):
        self.process_button(7, 10)

    def click_pushButtonK9(self):
        self.process_button(8, 10)

    def click_pushButtonK10(self):
        self.process_button(9, 10)

    def click_pushButtonK11(self):
        self.process_button(10, 10)

    def click_pushButtonK12(self):
        self.process_button(11, 10)

    def click_pushButtonK13(self):
        self.process_button(12, 10)

    def click_pushButtonK14(self):
        self.process_button(13, 10)

    def click_pushButtonK15(self):
        self.process_button(14, 10)

    def click_pushButtonL1(self):
        self.process_button(0, 11)

    def click_pushButtonL2(self):
        self.process_button(1, 11)

    def click_pushButtonL3(self):
        self.process_button(2, 11)

    def click_pushButtonL4(self):
        self.process_button(3, 11)

    def click_pushButtonL5(self):
        self.process_button(4, 11)

    def click_pushButtonL6(self):
        self.process_button(5, 11)

    def click_pushButtonL7(self):
        self.process_button(6, 11)

    def click_pushButtonL8(self):
        self.process_button(7, 11)

    def click_pushButtonL9(self):
        self.process_button(8, 11)

    def click_pushButtonL10(self):
        self.process_button(9, 11)

    def click_pushButtonL11(self):
        self.process_button(10, 11)

    def click_pushButtonL12(self):
        self.process_button(11, 11)

    def click_pushButtonL13(self):
        self.process_button(12, 11)

    def click_pushButtonL14(self):
        self.process_button(13, 11)

    def click_pushButtonL15(self):
        self.process_button(14, 11)

    def click_pushButtonM1(self):
        self.process_button(0, 12)

    def click_pushButtonM2(self):
        self.process_button(1, 12)

    def click_pushButtonM3(self):
        self.process_button(2, 12)

    def click_pushButtonM4(self):
        self.process_button(3, 12)

    def click_pushButtonM5(self):
        self.process_button(4, 12)

    def click_pushButtonM6(self):
        self.process_button(5, 12)

    def click_pushButtonM7(self):
        self.process_button(6, 12)

    def click_pushButtonM8(self):
        self.process_button(7, 12)

    def click_pushButtonM9(self):
        self.process_button(8, 12)

    def click_pushButtonM10(self):
        self.process_button(9, 12)

    def click_pushButtonM11(self):
        self.process_button(10, 12)

    def click_pushButtonM12(self):
        self.process_button(11, 12)

    def click_pushButtonM13(self):
        self.process_button(12, 12)

    def click_pushButtonM14(self):
        self.process_button(13, 12)

    def click_pushButtonM15(self):
        self.process_button(14, 12)

    def click_pushButtonN1(self):
        self.process_button(0, 13)

    def click_pushButtonN2(self):
        self.process_button(1, 13)

    def click_pushButtonN3(self):
        self.process_button(2, 13)

    def click_pushButtonN4(self):
        self.process_button(3, 13)

    def click_pushButtonN5(self):
        self.process_button(4, 13)

    def click_pushButtonN6(self):
        self.process_button(5, 13)

    def click_pushButtonN7(self):
        self.process_button(6, 13)

    def click_pushButtonN8(self):
        self.process_button(7, 13)

    def click_pushButtonN9(self):
        self.process_button(8, 13)

    def click_pushButtonN10(self):
        self.process_button(9, 13)

    def click_pushButtonN11(self):
        self.process_button(10, 13)

    def click_pushButtonN12(self):
        self.process_button(11, 13)

    def click_pushButtonN13(self):
        self.process_button(12, 13)

    def click_pushButtonN14(self):
        self.process_button(13, 13)

    def click_pushButtonN15(self):
        self.process_button(14, 13)

    def click_pushButtonO1(self):
        self.process_button(0, 14)

    def click_pushButtonO2(self):
        self.process_button(1, 14)

    def click_pushButtonO3(self):
        self.process_button(2, 14)

    def click_pushButtonO4(self):
        self.process_button(3, 14)

    def click_pushButtonO5(self):
        self.process_button(4, 14)

    def click_pushButtonO6(self):
        self.process_button(5, 14)

    def click_pushButtonO7(self):
        self.process_button(6, 14)

    def click_pushButtonO8(self):
        self.process_button(7, 14)

    def click_pushButtonO9(self):
        self.process_button(8, 14)

    def click_pushButtonO10(self):
        self.process_button(9, 14)

    def click_pushButtonO11(self):
        self.process_button(10, 14)

    def click_pushButtonO12(self):
        self.process_button(11, 14)

    def click_pushButtonO13(self):
        self.process_button(12, 14)

    def click_pushButtonO14(self):
        self.process_button(13, 14)

    def click_pushButtonO15(self):
        self.process_button(14, 14)

    def init_game_configs(self):
        self.buttons_flagged = 0
        self.flag_label.setText("Flag OFF")
        self.pushButtonFlag.status = False
        self.erase_board()
        # Raffle buttons
        self.bombs_position_raffle()
        # Init other fields
        self.define_other_fields()
        self.time = QTime(0, 0, 0)
        self.timer.start(1000)
        self.timer_label.setText("00:00:00")
        self.bombs_label.setText(f"{self.buttons_flagged}/{Ui_MainWindow.QUANTITY_BOMBS}")
        self.centralwidget.setCursor(QCursor(QtCore.Qt.CustomCursor))

    def process_button(self, x, y):
        if not self.board[y][x].isCheckable():
            return
        if self.pushButtonFlag.status:
            if self.board[y][x].is_flag:
                icon = self.show_image('g')
                self.board[y][x].is_flag = False
                self.buttons_flagged -= 1
            else:
                icon = self.show_image('f')
                self.board[y][x].is_flag = True
                self.buttons_flagged += 1
            self.board[y][x].setIcon(icon)
            self.board[y][x].setIconSize(QSize(28, 28))
            self.bombs_label.setText(f"{self.buttons_flagged}/{Ui_MainWindow.QUANTITY_BOMBS}")
            return
        if self.board[y][x].is_flag:
            return
        icon = self.show_image(self.board[y][x].value)
        self.board[y][x].setCheckable(False)
        self.board[y][x].setIcon(icon)
        self.board[y][x].setIconSize(QSize(28, 28))
        if self.board[y][x].value == 'b':
            self.end_game(Ui_MainWindow.DEFEAT)
        elif self.board[y][x].value == '0':
            self.process_neighbour_buttons(x, y)
        if self.check_fields_checkable() == Ui_MainWindow.QUANTITY_FIELDS:
            self.end_game(Ui_MainWindow.VICTORY)

    def check_fields_checkable(self):
        count_not_checkable = 0
        for y in range(0, Ui_MainWindow.LENGTH_AXIS_Y):
            for x in range(0, Ui_MainWindow.LENGTH_AXIS_X):
                if not self.board[y][x].isCheckable():
                    count_not_checkable += 1
        return count_not_checkable

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
        elif value == 'f':
            icon = self.icons.get_icon_flag()
        elif value == 'g':
            icon = self.icons.get_icon_gray()
        else:
            raise "Invalid value"
        return icon

    def bombs_position_raffle(self):
        quant_bombs = 0
        while quant_bombs < Ui_MainWindow.QUANTITY_BOMBS:
            x = randint(0, Ui_MainWindow.LENGTH_AXIS_X - 1)
            y = randint(0, Ui_MainWindow.LENGTH_AXIS_Y - 1)
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

    def end_game(self, status):
        self.timer.stop()
        msgBox = QMessageBox()
        if status == Ui_MainWindow.DEFEAT:
            text = "You lose"
        elif status == Ui_MainWindow.VICTORY:
            text = f"You win. Your time - {self.time.toString('hh:mm:ss')}"
        else:
            raise "Invalid status"
        ret = msgBox.question(self, 'End game', f"{text}\nDo you want to play again?",
                              QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            self.init_game_configs()
        else:
            sys.exit()

    def toggle_flag_status(self):
        self.pushButtonFlag.status = True if self.pushButtonFlag.status == False else False
        self.flag_label.setText("Flag OFF" if self.pushButtonFlag.status == False else "Flag ON")
        self.centralwidget.setCursor(QCursor(QtCore.Qt.CustomCursor if self.pushButtonFlag.status == False
                                             else QtCore.Qt.PointingHandCursor))

    def timer_event(self):
        self.time = self.time.addSecs(1)
        self.timer_label.setText(self.time.toString("hh:mm:ss"))


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
