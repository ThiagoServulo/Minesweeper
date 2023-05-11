from PySide2.QtWidgets import *
from PySide2.QtCore import *
from Constants import Constants
from Icon import Icon


class Board(Icon):
    def __init__(self):
        """
        Constructor
        """
        Icon.__init__(self)
        # Board buttons matrix
        self.board = []
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

    def create_board(self):
        """
        Create the board
        """
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

    def erase_board(self):
        """
        Erase entire board
        """
        for i in range(Constants.LENGTH_AXIS_Y):
            for j in range(Constants.LENGTH_AXIS_X):
                self.board[i][j].value = '0'
                icon = self.get_icon('g')
                self.board[i][j].setIcon(icon)
                self.board[i][j].setIconSize(QSize(28, 28))
                self.board[i][j].is_flag = False
                self.board[i][j].setCheckable(True)
