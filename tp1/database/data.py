import sqlite3


class Data:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('./database/database.db')
        return self.connection

    def check(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        return cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='article';")

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def read(self):
        connection = self.get_connection()
        cursor = connection.cursor()
        return cursor.execute("SELECT * FROM article;")

    # this methode is used for inter command
    def inter_command(self, arg):
        connection = self.get_connection()
        cursor = connection.cursor()
        return cursor.execute(arg)

    # commit changes to bd
    def commit(self):
        self.get_connection().commit()

    # creat table
    def create_table(self, text):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(text)
        self.get_connection().commit()

    # def execute(self, command):
    #   connection=self.get_connection()
    #  cursor=connection.cursor()
    # self.cursor().execute(command)
