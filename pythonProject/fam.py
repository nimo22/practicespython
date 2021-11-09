import  cout
class gage(cout.count):
    def __init__(self,sex,origin,name,age,degree,kids):
        self.kids=kids
        super().__init__(sex,origin,name,age,degree)


    def doeskid(self):
        print("yes") if self.kids>3 else print("no")