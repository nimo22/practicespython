class Fc:
    def __init__(self):
        pass

    def html(self, balise):
        def inside(text):
            print("<{0}>{1}<{0}>".format(balise, text))

        return inside
