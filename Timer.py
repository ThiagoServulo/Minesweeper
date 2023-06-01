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
        self.timer_paused = False

    def init_timer(self):
        """
        Initialize the timer
        """
        self.time = QTime(0, 0, 0)
        self.timer.start(1000)
        self.timer_label.setText("00:00:00")
        self.timer_paused = False

    def pause_timer(self):
        """
        Pause the timer
        """
        self.timer_paused = True

    def resume_timer(self):
        """
        Resume the timer
        """
        self.timer_paused = False

    def timer_event(self):
        """
        Event to timer trigged
        """
        if not self.timer_paused:
            self.time = self.time.addSecs(1)
            self.timer_label.setText(self.time.toString("hh:mm:ss"))
