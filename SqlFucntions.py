import sqlite3


class SqlFunctions:

    DATABASE_NAME = 'minesweeper.db'

    def __init__(self):
        """
        Constructor
        """
        self.connection = None
        self.cursor = None

    def init_connection(self):
        """
        Init database connection
        """
        self.connection = sqlite3.connect(SqlFunctions.DATABASE_NAME)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS best_times (time_seconds int)''')

    def close_connection(self):
        """
        Close database connection
        """
        self.connection.close()

    def drop_table_best_times(self):
        """
        Drop best_times table
        """
        self.init_connection()
        self.cursor.execute("DROP TABLE best_times")
        self.close_connection()

    def insert_time(self, time_seconds: int):
        """
        Inset time into database
        :param time_seconds: time in seconds
        """
        self.init_connection()
        self.cursor.execute("INSERT INTO best_times (time_seconds) VALUES (?)", (time_seconds,))
        self.connection.commit()
        self.close_connection()

    def select_times(self) -> list[int]:
        """
        Select the five best times from database
        :return: list with the five best times
        """
        self.init_connection()
        self.cursor.execute("SELECT * FROM best_times ORDER BY time_seconds ASC LIMIT 5")
        best_times = self.cursor.fetchall()
        self.close_connection()
        return [time for tuple_time in best_times for time in tuple_time]