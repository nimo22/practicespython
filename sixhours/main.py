from flask import Flask
from factory import Fac
from file.handler import File
from db.data import Db

if __name__ == '__main__':
    data_base = Db()
    script=File()
    data_base.execute(script.read("./db/db.sql"))
