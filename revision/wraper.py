
class Wraper:
    def __init__(self):
        pass

    def wrap(func):
        def insi():
            return func()

        return insi
    @wrap
    def run(self):
        print("runing")
