class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(f"this is my firstname ={self.firstname}")


class Student(Person):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        super().__init__(fname, lname)


x = Student("Mike", "Olsen")
print(x.fname)
x.printname()
