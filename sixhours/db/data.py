import sqlite3


class Db:
    def __init__(self):
        self.connection = None

    # noinspection PyMethodMayBeStatic
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("data.db")
            self.connection.row_factory = sqlite3.Row

        return self.connection

    # noinspection PyMethodMayBeStatic
    def disconnect(self):
        if self.connection is not None:
            self.connect().close()
            self.connection = None

    def admit(self):
        self.connect().commit()

    # noinspection PyMethodMayBeStatic
    def cursor(self):
        return self.connect().cursor()

    def execute(self, script):
        self.cursor().executescript(script)
