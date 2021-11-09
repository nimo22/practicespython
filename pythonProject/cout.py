import creater
class count(creater.persone):
    def __init__(self,sex,origin,name,age,degree):
        self.age=age
        self.degree=degree
        super().__init__(sex,origin,name)


    def prof(self):
        print(self.degree+" "+self.age)