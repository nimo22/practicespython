from db.db import Data
from read.filereader import Reader
import os


class Re:
    def __init__(self):
        pass

    def redo(self):
        reader = Reader()
        db = Data()
        tiger = os.getcwd() + "\\documents\\table.sql"
        inpu = os.getcwd() + "\\documents\\data.sql"
        script = reader.read(tiger)
        if not os.path.exists(os.getcwd() + "\\data.db"):
            db.script(script)
        reader.close()
        db.insert(reader.read(inpu))
        db.commit()
        reader.close()
        db.disconnect()
