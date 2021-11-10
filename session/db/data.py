import sqlite3
import os

class Data:
    def __init__(self):
        self.token = None

    def connect(self):
        if self.token is None:
            self.conn = sqlite3.connect("./db/login.db")
            self.conn.row_factory = sqlite3.Row
        return self.conn

    def disconnect(self):
        if self.token is not None:
            sqlite3.connect("./db/login.db").close()
            self.token = None

    def commit(self):
        self.connect().commit()

    def cursor(self):
        return self.connect().cursor()

    def execute(self, script):
        self.cursor().executescript(script)
