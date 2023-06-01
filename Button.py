from PySide2.QtCore import *
from PyQt5.QtWidgets import QApplication
from Constants import Constants
from Board import Board


class Button(Board):
    def __init__(self):
        """
        Constructor
        """
        Board.__init__(self)
        self.function_click_buttons = []
        self.buttons_flagged = 0

    def process_button(self, x: int, y: int):
        """
        Process the event to click button
        :param x: Position of the button in the axis X
        :param y: Position of the button in the axis Y
        """
        # Check if the button is checkable
        if not self.board[y][x].isCheckable():
            return
        # Check the button flag status
        if self.pushButtonFlag.status:
            if self.board[y][x].is_flag:
                icon = self.get_icon('g')
                self.board[y][x].is_flag = False
                self.buttons_flagged -= 1
            else:
                icon = self.get_icon('ff')
                self.board[y][x].is_flag = True
                self.buttons_flagged += 1
            self.board[y][x].setIcon(icon)
            self.board[y][x].setIconSize(QSize(28, 28))
            self.bombs_label.setText(f"{self.buttons_flagged}/{Constants.QUANTITY_BOMBS}")
            return
        # Check if the field is a flag
        if self.board[y][x].is_flag:
            return
        icon = self.get_icon(self.board[y][x].value)
        self.board[y][x].setCheckable(False)
        self.board[y][x].setIcon(icon)
        self.board[y][x].setIconSize(QSize(28, 28))
        if self.board[y][x].value == 'b':
            self.end_game(Constants.DEFEAT)
        elif self.board[y][x].value == '0':
            self.process_neighbour_buttons(x, y)
        if self.count_fields_checkable() == Constants.QUANTITY_FIELDS:
            self.end_game(Constants.VICTORY)

    def create_button_functions(self):
        # First line
        self.pushButtonA1.clicked.connect(lambda: self.process_button(0, 0))
        self.pushButtonA2.clicked.connect(lambda: self.process_button(1, 0))
        self.pushButtonA3.clicked.connect(lambda: self.process_button(2, 0))
        self.pushButtonA4.clicked.connect(lambda: self.process_button(3, 0))
        self.pushButtonA5.clicked.connect(lambda: self.process_button(4, 0))
        self.pushButtonA6.clicked.connect(lambda: self.process_button(5, 0))
        self.pushButtonA7.clicked.connect(lambda: self.process_button(6, 0))
        self.pushButtonA8.clicked.connect(lambda: self.process_button(7, 0))
        self.pushButtonA9.clicked.connect(lambda: self.process_button(8, 0))
        self.pushButtonA10.clicked.connect(lambda: self.process_button(9, 0))
        self.pushButtonA11.clicked.connect(lambda: self.process_button(10, 0))
        self.pushButtonA12.clicked.connect(lambda: self.process_button(11, 0))
        self.pushButtonA13.clicked.connect(lambda: self.process_button(12, 0))
        self.pushButtonA14.clicked.connect(lambda: self.process_button(13, 0))
        self.pushButtonA15.clicked.connect(lambda: self.process_button(14, 0))
        # Second line
        self.pushButtonB1.clicked.connect(lambda: self.process_button(0, 1))
        self.pushButtonB2.clicked.connect(lambda: self.process_button(1, 1))
        self.pushButtonB3.clicked.connect(lambda: self.process_button(2, 1))
        self.pushButtonB4.clicked.connect(lambda: self.process_button(3, 1))
        self.pushButtonB5.clicked.connect(lambda: self.process_button(4, 1))
        self.pushButtonB6.clicked.connect(lambda: self.process_button(5, 1))
        self.pushButtonB7.clicked.connect(lambda: self.process_button(6, 1))
        self.pushButtonB8.clicked.connect(lambda: self.process_button(7, 1))
        self.pushButtonB9.clicked.connect(lambda: self.process_button(8, 1))
        self.pushButtonB10.clicked.connect(lambda: self.process_button(9, 1))
        self.pushButtonB11.clicked.connect(lambda: self.process_button(10, 1))
        self.pushButtonB12.clicked.connect(lambda: self.process_button(11, 1))
        self.pushButtonB13.clicked.connect(lambda: self.process_button(12, 1))
        self.pushButtonB14.clicked.connect(lambda: self.process_button(13, 1))
        self.pushButtonB15.clicked.connect(lambda: self.process_button(14, 1))
        # Third line
        self.pushButtonC1.clicked.connect(lambda: self.process_button(0, 2))
        self.pushButtonC2.clicked.connect(lambda: self.process_button(1, 2))
        self.pushButtonC3.clicked.connect(lambda: self.process_button(2, 2))
        self.pushButtonC4.clicked.connect(lambda: self.process_button(3, 2))
        self.pushButtonC5.clicked.connect(lambda: self.process_button(4, 2))
        self.pushButtonC6.clicked.connect(lambda: self.process_button(5, 2))
        self.pushButtonC7.clicked.connect(lambda: self.process_button(6, 2))
        self.pushButtonC8.clicked.connect(lambda: self.process_button(7, 2))
        self.pushButtonC9.clicked.connect(lambda: self.process_button(8, 2))
        self.pushButtonC10.clicked.connect(lambda: self.process_button(9, 2))
        self.pushButtonC11.clicked.connect(lambda: self.process_button(10, 2))
        self.pushButtonC12.clicked.connect(lambda: self.process_button(11, 2))
        self.pushButtonC13.clicked.connect(lambda: self.process_button(12, 2))
        self.pushButtonC14.clicked.connect(lambda: self.process_button(13, 2))
        self.pushButtonC15.clicked.connect(lambda: self.process_button(14, 2))
        # Fourth line
        self.pushButtonD1.clicked.connect(lambda: self.process_button(0, 3))
        self.pushButtonD2.clicked.connect(lambda: self.process_button(1, 3))
        self.pushButtonD3.clicked.connect(lambda: self.process_button(2, 3))
        self.pushButtonD4.clicked.connect(lambda: self.process_button(3, 3))
        self.pushButtonD5.clicked.connect(lambda: self.process_button(4, 3))
        self.pushButtonD6.clicked.connect(lambda: self.process_button(5, 3))
        self.pushButtonD7.clicked.connect(lambda: self.process_button(6, 3))
        self.pushButtonD8.clicked.connect(lambda: self.process_button(7, 3))
        self.pushButtonD9.clicked.connect(lambda: self.process_button(8, 3))
        self.pushButtonD10.clicked.connect(lambda: self.process_button(9, 3))
        self.pushButtonD11.clicked.connect(lambda: self.process_button(10, 3))
        self.pushButtonD12.clicked.connect(lambda: self.process_button(11, 3))
        self.pushButtonD13.clicked.connect(lambda: self.process_button(12, 3))
        self.pushButtonD14.clicked.connect(lambda: self.process_button(13, 3))
        self.pushButtonD15.clicked.connect(lambda: self.process_button(14, 3))
        # Fiveth line
        self.pushButtonE1.clicked.connect(lambda: self.process_button(0, 4))
        self.pushButtonE2.clicked.connect(lambda: self.process_button(1, 4))
        self.pushButtonE3.clicked.connect(lambda: self.process_button(2, 4))
        self.pushButtonE4.clicked.connect(lambda: self.process_button(3, 4))
        self.pushButtonE5.clicked.connect(lambda: self.process_button(4, 4))
        self.pushButtonE6.clicked.connect(lambda: self.process_button(5, 4))
        self.pushButtonE7.clicked.connect(lambda: self.process_button(6, 4))
        self.pushButtonE8.clicked.connect(lambda: self.process_button(7, 4))
        self.pushButtonE9.clicked.connect(lambda: self.process_button(8, 4))
        self.pushButtonE10.clicked.connect(lambda: self.process_button(9, 4))
        self.pushButtonE11.clicked.connect(lambda: self.process_button(10, 4))
        self.pushButtonE12.clicked.connect(lambda: self.process_button(11, 4))
        self.pushButtonE13.clicked.connect(lambda: self.process_button(12, 4))
        self.pushButtonE14.clicked.connect(lambda: self.process_button(13, 4))
        self.pushButtonE15.clicked.connect(lambda: self.process_button(14, 4))
        # Sixth line
        self.pushButtonF1.clicked.connect(lambda: self.process_button(0, 5))
        self.pushButtonF2.clicked.connect(lambda: self.process_button(1, 5))
        self.pushButtonF3.clicked.connect(lambda: self.process_button(2, 5))
        self.pushButtonF4.clicked.connect(lambda: self.process_button(3, 5))
        self.pushButtonF5.clicked.connect(lambda: self.process_button(4, 5))
        self.pushButtonF6.clicked.connect(lambda: self.process_button(5, 5))
        self.pushButtonF7.clicked.connect(lambda: self.process_button(6, 5))
        self.pushButtonF8.clicked.connect(lambda: self.process_button(7, 5))
        self.pushButtonF9.clicked.connect(lambda: self.process_button(8, 5))
        self.pushButtonF10.clicked.connect(lambda: self.process_button(9, 5))
        self.pushButtonF11.clicked.connect(lambda: self.process_button(10, 5))
        self.pushButtonF12.clicked.connect(lambda: self.process_button(11, 5))
        self.pushButtonF13.clicked.connect(lambda: self.process_button(12, 5))
        self.pushButtonF14.clicked.connect(lambda: self.process_button(13, 5))
        self.pushButtonF15.clicked.connect(lambda: self.process_button(14, 5))
        # Seventh line
        self.pushButtonG1.clicked.connect(lambda: self.process_button(0, 6))
        self.pushButtonG2.clicked.connect(lambda: self.process_button(1, 6))
        self.pushButtonG3.clicked.connect(lambda: self.process_button(2, 6))
        self.pushButtonG4.clicked.connect(lambda: self.process_button(3, 6))
        self.pushButtonG5.clicked.connect(lambda: self.process_button(4, 6))
        self.pushButtonG6.clicked.connect(lambda: self.process_button(5, 6))
        self.pushButtonG7.clicked.connect(lambda: self.process_button(6, 6))
        self.pushButtonG8.clicked.connect(lambda: self.process_button(7, 6))
        self.pushButtonG9.clicked.connect(lambda: self.process_button(8, 6))
        self.pushButtonG10.clicked.connect(lambda: self.process_button(9, 6))
        self.pushButtonG11.clicked.connect(lambda: self.process_button(10, 6))
        self.pushButtonG12.clicked.connect(lambda: self.process_button(11, 6))
        self.pushButtonG13.clicked.connect(lambda: self.process_button(12, 6))
        self.pushButtonG14.clicked.connect(lambda: self.process_button(13, 6))
        self.pushButtonG15.clicked.connect(lambda: self.process_button(14, 6))
        # Eighth line
        self.pushButtonH1.clicked.connect(lambda: self.process_button(0, 7))
        self.pushButtonH2.clicked.connect(lambda: self.process_button(1, 7))
        self.pushButtonH3.clicked.connect(lambda: self.process_button(2, 7))
        self.pushButtonH4.clicked.connect(lambda: self.process_button(3, 7))
        self.pushButtonH5.clicked.connect(lambda: self.process_button(4, 7))
        self.pushButtonH6.clicked.connect(lambda: self.process_button(5, 7))
        self.pushButtonH7.clicked.connect(lambda: self.process_button(6, 7))
        self.pushButtonH8.clicked.connect(lambda: self.process_button(7, 7))
        self.pushButtonH9.clicked.connect(lambda: self.process_button(8, 7))
        self.pushButtonH10.clicked.connect(lambda: self.process_button(9, 7))
        self.pushButtonH11.clicked.connect(lambda: self.process_button(10, 7))
        self.pushButtonH12.clicked.connect(lambda: self.process_button(11, 7))
        self.pushButtonH13.clicked.connect(lambda: self.process_button(12, 7))
        self.pushButtonH14.clicked.connect(lambda: self.process_button(13, 7))
        self.pushButtonH15.clicked.connect(lambda: self.process_button(14, 7))
        # Nineth line
        self.pushButtonI1.clicked.connect(lambda: self.process_button(0, 8))
        self.pushButtonI2.clicked.connect(lambda: self.process_button(1, 8))
        self.pushButtonI3.clicked.connect(lambda: self.process_button(2, 8))
        self.pushButtonI4.clicked.connect(lambda: self.process_button(3, 8))
        self.pushButtonI5.clicked.connect(lambda: self.process_button(4, 8))
        self.pushButtonI6.clicked.connect(lambda: self.process_button(5, 8))
        self.pushButtonI7.clicked.connect(lambda: self.process_button(6, 8))
        self.pushButtonI8.clicked.connect(lambda: self.process_button(7, 8))
        self.pushButtonI9.clicked.connect(lambda: self.process_button(8, 8))
        self.pushButtonI10.clicked.connect(lambda: self.process_button(9, 8))
        self.pushButtonI11.clicked.connect(lambda: self.process_button(10, 8))
        self.pushButtonI12.clicked.connect(lambda: self.process_button(11, 8))
        self.pushButtonI13.clicked.connect(lambda: self.process_button(12, 8))
        self.pushButtonI14.clicked.connect(lambda: self.process_button(13, 8))
        self.pushButtonI15.clicked.connect(lambda: self.process_button(14, 8))
        # Tenth line
        self.pushButtonJ1.clicked.connect(lambda: self.process_button(0, 9))
        self.pushButtonJ2.clicked.connect(lambda: self.process_button(1, 9))
        self.pushButtonJ3.clicked.connect(lambda: self.process_button(2, 9))
        self.pushButtonJ4.clicked.connect(lambda: self.process_button(3, 9))
        self.pushButtonJ5.clicked.connect(lambda: self.process_button(4, 9))
        self.pushButtonJ6.clicked.connect(lambda: self.process_button(5, 9))
        self.pushButtonJ7.clicked.connect(lambda: self.process_button(6, 9))
        self.pushButtonJ8.clicked.connect(lambda: self.process_button(7, 9))
        self.pushButtonJ9.clicked.connect(lambda: self.process_button(8, 9))
        self.pushButtonJ10.clicked.connect(lambda: self.process_button(9, 9))
        self.pushButtonJ11.clicked.connect(lambda: self.process_button(10, 9))
        self.pushButtonJ12.clicked.connect(lambda: self.process_button(11, 9))
        self.pushButtonJ13.clicked.connect(lambda: self.process_button(12, 9))
        self.pushButtonJ14.clicked.connect(lambda: self.process_button(13, 9))
        self.pushButtonJ15.clicked.connect(lambda: self.process_button(14, 9))
        # Eleventh line
        self.pushButtonK1.clicked.connect(lambda: self.process_button(0, 10))
        self.pushButtonK2.clicked.connect(lambda: self.process_button(1, 10))
        self.pushButtonK3.clicked.connect(lambda: self.process_button(2, 10))
        self.pushButtonK4.clicked.connect(lambda: self.process_button(3, 10))
        self.pushButtonK5.clicked.connect(lambda: self.process_button(4, 10))
        self.pushButtonK6.clicked.connect(lambda: self.process_button(5, 10))
        self.pushButtonK7.clicked.connect(lambda: self.process_button(6, 10))
        self.pushButtonK8.clicked.connect(lambda: self.process_button(7, 10))
        self.pushButtonK9.clicked.connect(lambda: self.process_button(8, 10))
        self.pushButtonK10.clicked.connect(lambda: self.process_button(9, 10))
        self.pushButtonK11.clicked.connect(lambda: self.process_button(10, 10))
        self.pushButtonK12.clicked.connect(lambda: self.process_button(11, 10))
        self.pushButtonK13.clicked.connect(lambda: self.process_button(12, 10))
        self.pushButtonK14.clicked.connect(lambda: self.process_button(13, 10))
        self.pushButtonK15.clicked.connect(lambda: self.process_button(14, 10))
        # Twelveth line
        self.pushButtonL1.clicked.connect(lambda: self.process_button(0, 11))
        self.pushButtonL2.clicked.connect(lambda: self.process_button(1, 11))
        self.pushButtonL3.clicked.connect(lambda: self.process_button(2, 11))
        self.pushButtonL4.clicked.connect(lambda: self.process_button(3, 11))
        self.pushButtonL5.clicked.connect(lambda: self.process_button(4, 11))
        self.pushButtonL6.clicked.connect(lambda: self.process_button(5, 11))
        self.pushButtonL7.clicked.connect(lambda: self.process_button(6, 11))
        self.pushButtonL8.clicked.connect(lambda: self.process_button(7, 11))
        self.pushButtonL9.clicked.connect(lambda: self.process_button(8, 11))
        self.pushButtonL10.clicked.connect(lambda: self.process_button(9, 11))
        self.pushButtonL11.clicked.connect(lambda: self.process_button(10, 11))
        self.pushButtonL12.clicked.connect(lambda: self.process_button(11, 11))
        self.pushButtonL13.clicked.connect(lambda: self.process_button(12, 11))
        self.pushButtonL14.clicked.connect(lambda: self.process_button(13, 11))
        self.pushButtonL15.clicked.connect(lambda: self.process_button(14, 11))
        # Thirteenth line
        self.pushButtonM1.clicked.connect(lambda: self.process_button(0, 12))
        self.pushButtonM2.clicked.connect(lambda: self.process_button(1, 12))
        self.pushButtonM3.clicked.connect(lambda: self.process_button(2, 12))
        self.pushButtonM4.clicked.connect(lambda: self.process_button(3, 12))
        self.pushButtonM5.clicked.connect(lambda: self.process_button(4, 12))
        self.pushButtonM6.clicked.connect(lambda: self.process_button(5, 12))
        self.pushButtonM7.clicked.connect(lambda: self.process_button(6, 12))
        self.pushButtonM8.clicked.connect(lambda: self.process_button(7, 12))
        self.pushButtonM9.clicked.connect(lambda: self.process_button(8, 12))
        self.pushButtonM10.clicked.connect(lambda: self.process_button(9, 12))
        self.pushButtonM11.clicked.connect(lambda: self.process_button(10, 12))
        self.pushButtonM12.clicked.connect(lambda: self.process_button(11, 12))
        self.pushButtonM13.clicked.connect(lambda: self.process_button(12, 12))
        self.pushButtonM14.clicked.connect(lambda: self.process_button(13, 12))
        self.pushButtonM15.clicked.connect(lambda: self.process_button(14, 12))
        # Fourteenth line
        self.pushButtonN1.clicked.connect(lambda: self.process_button(0, 13))
        self.pushButtonN2.clicked.connect(lambda: self.process_button(1, 13))
        self.pushButtonN3.clicked.connect(lambda: self.process_button(2, 13))
        self.pushButtonN4.clicked.connect(lambda: self.process_button(3, 13))
        self.pushButtonN5.clicked.connect(lambda: self.process_button(4, 13))
        self.pushButtonN6.clicked.connect(lambda: self.process_button(5, 13))
        self.pushButtonN7.clicked.connect(lambda: self.process_button(6, 13))
        self.pushButtonN8.clicked.connect(lambda: self.process_button(7, 13))
        self.pushButtonN9.clicked.connect(lambda: self.process_button(8, 13))
        self.pushButtonN10.clicked.connect(lambda: self.process_button(9, 13))
        self.pushButtonN11.clicked.connect(lambda: self.process_button(10, 13))
        self.pushButtonN12.clicked.connect(lambda: self.process_button(11, 13))
        self.pushButtonN13.clicked.connect(lambda: self.process_button(12, 13))
        self.pushButtonN14.clicked.connect(lambda: self.process_button(13, 13))
        self.pushButtonN15.clicked.connect(lambda: self.process_button(14, 13))
        # Fiveteenth line
        self.pushButtonO1.clicked.connect(lambda: self.process_button(0, 14))
        self.pushButtonO2.clicked.connect(lambda: self.process_button(1, 14))
        self.pushButtonO3.clicked.connect(lambda: self.process_button(2, 14))
        self.pushButtonO4.clicked.connect(lambda: self.process_button(3, 14))
        self.pushButtonO5.clicked.connect(lambda: self.process_button(4, 14))
        self.pushButtonO6.clicked.connect(lambda: self.process_button(5, 14))
        self.pushButtonO7.clicked.connect(lambda: self.process_button(6, 14))
        self.pushButtonO8.clicked.connect(lambda: self.process_button(7, 14))
        self.pushButtonO9.clicked.connect(lambda: self.process_button(8, 14))
        self.pushButtonO10.clicked.connect(lambda: self.process_button(9, 14))
        self.pushButtonO11.clicked.connect(lambda: self.process_button(10, 14))
        self.pushButtonO12.clicked.connect(lambda: self.process_button(11, 14))
        self.pushButtonO13.clicked.connect(lambda: self.process_button(12, 14))
        self.pushButtonO14.clicked.connect(lambda: self.process_button(13, 14))
        self.pushButtonO15.clicked.connect(lambda: self.process_button(14, 14))

    @staticmethod
    def get_range_limits(x: int, y: int) -> (int, int, int, int):
        """
        Get the range axis limits
        :param x: Center value in the axis X
        :param y: Center value in the axis Y
        :return: Range limits (x_min, x_max, y_min, y_max)
        """
        x_min: int = 0 if x - 1 < 0 else x - 1
        x_max: int = Constants.LENGTH_AXIS_X if x + 2 > Constants.LENGTH_AXIS_X else x + 2
        y_min: int = 0 if y - 1 < 0 else y - 1
        y_max: int = Constants.LENGTH_AXIS_Y if y + 2 > Constants.LENGTH_AXIS_Y else y + 2
        return x_min, x_max, y_min, y_max

    def process_neighbour_buttons(self, x: int, y: int):
        """
        Process the neighbour of the buttons
        :param x: Value in the axis X
        :param y: Value in the axis Y
        """
        x_min, x_max, y_min, y_max = self.get_range_limits(x, y)
        for i in range(x_min, x_max):
            for j in range(y_min, y_max):
                if self.board[j][i].isCheckable():
                    self.process_button(i, j)
