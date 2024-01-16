def a():
    print("a() starts")
    b()
    d()
    print("a() ends")


def b():
    print("b() starts")
    c()
    print("b() ends")


def c():
    print("c() starts")
    print("c() ends")


def d():
    print("d() starts")
    print("d() ends")


a()
