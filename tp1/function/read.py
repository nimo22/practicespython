class Read:
    def __init__(self):
        self.file = None
        self.error = None
        self.file_string = None

    def readfile(self):
        try:
            self.file = open("./function/script.txt", "r")
            self.file_string = self.file.read()
            return self.file_string
        except OSError:
            return -1
