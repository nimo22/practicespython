
class Reader:
    def __init__(self):
        self.connection = False
        self.content = None

    def read(self, path):
        if self.connection is False:
            try:

                self.content = open(path, "rt", encoding="utf-8")
                self.connection = True
                return self.content.read()

            except Exception as e:
                print(e)

    def close(self):
        if self.connection is True:
            self.content.close()
            self.connection=False
