from PySide2.QtCore import *
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
                icon = self.get_icon('f')
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
        # Set the click button fuctions
        for i in range(Constants.LENGTH_AXIS_Y):
            for j in range(Constants.LENGTH_AXIS_X):
                self.board[i][j].clicked.connect(self.function_click_buttons[i][j])

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
                    self.function_click_buttons[j][i]()
