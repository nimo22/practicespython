class persone:
    def __init__(self,sex,origin,name):
        self.sex=sex
        self.origin=origin
        self.name=name
    def introduction(self):
        print("this is a persone is a :"+self.sex+"and her name is :"+self.name)
