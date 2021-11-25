import sqlite3


class Data:
    def __init__(self):
        self.con = False

    def get_connection(self):
        if self.con is False:
            self.con = sqlite3.connect("data.db")
            return self.con
        else:
            return self.con

    def disconnect(self):
        if self.con is not False:
            self.get_connection().close()
            self.con = False

    def cursor(self):
        return self.get_connection().cursor()

    def insert(self, data):
        self.cursor().execute(data)

    def script(self, script):
        self.cursor().executescript(script)

    def commit(self):

        self.get_connection().commit()
