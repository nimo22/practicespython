import os


class File:
    def __init__(self):
        self.r = None

    # noinspection PyMethodMayBeStatic
    def read(self, path):
        if self.r is None:
            if os.path.exists(path):
                self.r = open(path, "rt", encoding="utf-8")
                return self.r.read()
            else:
                print("file is not found")

    def cl(self):
        if self.r is not None:
            self.r.close()
