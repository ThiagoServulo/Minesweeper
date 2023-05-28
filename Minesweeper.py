import sys
from random import randint
from PySide2 import QtCore
from PySide2.QtGui import QCursor
from PySide2.QtWidgets import *
from typing import Literal
from Constants import Constants
from Layout import Layout


class Minesweeper(Layout):
    def setupUi(self, game_window):
        """
        Initialize the game window and its settings
        :param game_window: Window for the game
        """
        Layout.__init__(self, game_window)
        # Create board
        self.create_board()
        # Create button fucntions
        self.create_button_functions()
        # Initialize game settings
        self.initialize_game_settings()

    def initialize_game_settings(self):
        """
        Initialize the game settings
        """
        # Erase the board
        self.erase_board()
        # Raffle the bombs position
        self.buttons_flagged = 0
        self.pushButtonFlag.status = False
        self.raffle_bombs_position()
        # Reset timer
        self.init_timer()
        # Init labels and cursor
        self.bombs_label.setText(f"{self.buttons_flagged}/{Constants.QUANTITY_BOMBS}")
        self.centralwidget.setCursor(QCursor(QtCore.Qt.CustomCursor))
        # Set other fields
        self.set_other_fields()

    def count_fields_checkable(self) -> int:
        """
        Count the amount of the fields that not checkable
        :return: Amount of the fields that not checkable
        """
        count_not_checkable: int = 0
        # Loop for the board
        for y in range(0, Constants.LENGTH_AXIS_Y):
            for x in range(0, Constants.LENGTH_AXIS_X):
                # Check if the field is checkable
                if not self.board[y][x].isCheckable():
                    count_not_checkable += 1
        return count_not_checkable

    def raffle_bombs_position(self):
        """
        Raffle the bombs positions in the board
        """
        quant_bombs: int = 0
        while quant_bombs < Constants.QUANTITY_BOMBS:
            x: int = randint(0, Constants.LENGTH_AXIS_X - 1)
            y: int = randint(0, Constants.LENGTH_AXIS_Y - 1)
            # Check if there is already a bomb in this field
            if self.board[y][x].value != "b":
                self.board[y][x].value = "b"
                quant_bombs += 1

    def set_other_fields(self):
        """
        Set the other fields with the numbers
        """""
        for y in range(0, Constants.LENGTH_AXIS_Y):
            for x in range(0, Constants.LENGTH_AXIS_X):
                if self.board[y][x].value != 'b':
                    count_bombs: int = 0
                    for i in range(y - 1, y + 2):
                        for j in range(x - 1, x + 2):
                            if not ((i, j) == (y, x) or i < 0 or j < 0 or i >= Constants.LENGTH_AXIS_Y or
                                    j >= Constants.LENGTH_AXIS_X):
                                # Counting bombs
                                if self.board[i][j].value == 'b':
                                    count_bombs += 1
                    # Setting number of the field
                    self.board[y][x].value = str(count_bombs)

    def end_game(self, status: Literal[Constants.DEFEAT, Constants.VICTORY]):
        """
        Finish the game and show the Message Box
        :param status: Status of the game (vicotory or defeat)
        """
        # Stop the timer
        self.timer.stop()
        # Show message box
        msgBox: QMessageBox = QMessageBox()
        if status == Constants.DEFEAT:
            text: str = "You lose"
        elif status == Constants.VICTORY:
            text: str = f"You win. Your time - {self.time.toString('hh:mm:ss')}"
        else:
            raise "Invalid status"
        ret = msgBox.question(self, 'End game', f"{text}\nDo you want to play again?",
                              QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ret == QMessageBox.Yes:
            # Restart the game
            self.initialize_game_settings()
        else:
            # Finish the game
            sys.exit()

    def toggle_flag_status(self):
        """
        Toggle the flag status (on or off), changing the button, the label and the cursor
        """
        self.pushButtonFlag.status = True if self.pushButtonFlag.status == False else False
        self.pushButtonFlag.setIcon(self.icon_flag_on if self.pushButtonFlag.status else self.icon_flag_off)
        self.centralwidget.setCursor(QCursor(QtCore.Qt.CustomCursor if self.pushButtonFlag.status == False
                                             else QtCore.Qt.PointingHandCursor))
