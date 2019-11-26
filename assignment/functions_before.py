a = 0


def a_getter():
    print(a)
    return a


def increment():
    a += 1
    print(a)
    return a


def make_incrementor():
    x = 0
    print(x)

    def incrementor():
        x += 1
        print(x)
        return x

    def x_getter():
        print(x)
        return x

    return incrementor, x_getter