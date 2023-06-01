from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QFont
from SqlFucntions import SqlFunctions

class Actions(SqlFunctions):
    def __int__(self):
        """
        Constructor
        """
        SqlFunctions.__init__(self)

    def show_records(self):
        """
        Show a Message Box with the best times
        """
        font = QFont()
        font.setPointSize(10)
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Best Times")
        messageBox.setFont(font)
        times = self.get_times()
        if times == []:
            message = "You haven't records yet !"
        else:
            message = '\n'.join(f'{i+1} - {time}\t' for i, time in enumerate(times))
        messageBox.setText(message)
        messageBox.exec()

    def erase_records(self):
        """
        Erase all the times from database
        """
        font = QFont()
        font.setPointSize(10)
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Delete records")
        messageBox.setText("Are you sure to delete the records ?")
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        messageBox.setDefaultButton(QMessageBox.No)
        messageBox.setFont(font)
        if messageBox.exec_() == QMessageBox.Yes:
            self.drop_table_best_times()

    def save_time(self, time: str):
        """
        Save player time
        :param time: Player time
        """
        self.insert_time(self.convert_time_to_seconds(time))

    def get_times(self) -> list[str]:
        """
        Get the five best times
        :return: list of best times
        """
        times = self.select_times()
        return list(map(self.convert_secods_to_time, times))

    @staticmethod
    def convert_secods_to_time(seconds: int) -> str:
        """
        Convert seconds to time
        :param seconds: seconds in integer format
        :return: Time string in hh:mm:ss format
        """
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 3600) % 60
        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    @staticmethod
    def convert_time_to_seconds(time: str) -> int:
        """
        Convert time to seconds
        :param time: time string in hh:mm:ss format
        :return: Seconds in integer format
        """
        time = time.split(":")
        return (int(time[0]) * 3600) + (int(time[1]) * 60) + int(time[2])
