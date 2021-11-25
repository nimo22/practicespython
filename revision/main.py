from first_class_function import Fc
def adder(*numebers):
    y = 0
    for x in numebers:
        y = y + x
    print(y)


def siteur(**kwargs):
    for x in kwargs:
        print(x)


if __name__ == '__main__':
    adder(10, 10)
    dic={
        "Firstname" : {"Sita":10,"dsa":123},
        "Lastname" : "Sharma",
        "Age" : 22,
        "Phone" : 1234567890
    }

    siteur(**dic)
    x=3
    print("log",x)
    print(f"log {x}")
    ####################################################################
    fc=Fc()
    func=fc.html
    writer=func("h1")
    writer("hello world!")
