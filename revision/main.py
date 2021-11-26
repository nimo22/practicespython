from first_class_function import Fc
from wraper import Wraper
from datetime import d

def adder(*numebers):
    y = 0
    for x in numebers:
        y = y + x
    print(y)




def siteur(**kwargs):
    for x in kwargs:
        print(x)


def wrap(func):
    def insi():
        print("hi")
        return func()

    return insi


@wrap  # run=wrap(run)
def run():
    print("runing")


def essay(func):
    def arguments(*args, **kwargs):
        print("inside arguments")
        for x in args:
            print(x)
        for x in kwargs:
            print(x)
        return func(*args, **kwargs)

    return arguments


def fun(fun):
    day = date.today()

    def re(*args, **kwargs):
        print(day)
        return fun(*args,**kwargs)

    return re


@fun
def work(minutes, hours):
    print("aujourd hui je veux travailler {1} et {0} ".format(minutes, hours))


@essay
def call_it():
    print("calling it ")


@essay
def calcule(x, y):
    print("hi")
    print(x + y)


if __name__ == '__main__':
    run()
    adder(10, 10)
    dic = {
        "Firstname": {"Sita": 10, "dsa": 123},
        "Lastname": "Sharma",
        "Age": 22,
        "Phone": 1234567890
    }

    siteur(**dic)
    x = 3
    print("log", x)
    print(f"log {x}")
    ####################################################################
    fc = Fc()
    func = fc.html
    writer = func("h1")
    writer("hello world!")
    ##########################################################
    wr = Wraper()
    x = wrap(wr.run)
    run()
    call_it()
    print("=================")
    calcule(1, 2)
    work(0,12)
