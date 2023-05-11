from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Timer:
    def __init__(self):
        """
        Constructor
        """
        self.time = QTime()
        self.timer_label = QLabel()
        self.timer = QTimer()
        self.init_timer()

    def init_timer(self):
        """
        Initialize the timer
        """
        self.time = QTime(0, 0, 0)
        self.timer.start(1000)
        self.timer_label.setText("00:00:00")

    def timer_event(self):
        """
        Event to timer trigged
        """
        self.time = self.time.addSecs(1)
        self.timer_label.setText(self.time.toString("hh:mm:ss"))
