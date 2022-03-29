from input import *


def paraboll_method(a, b, epsilon, k=1):
    x1 = a
    x2 = (a + b) / 2
    x3 = b
    my_counter = Counter()
    func1 = f(my_counter, x1)
    func2 = f(my_counter, x2)
    func3 = f(my_counter, x3)
    funcU = 0
    u = 0
    while x3 - x1 > epsilon:
        k += 1
        z1 = ((x2 - x1) ** 2 * (func2 - func3) - (x2 - x3) ** 2 * (func2 - func1))
        z2 = (2 * ((x2 - x1) * (func2 - func3) - (x2 - x3) * (func2 - func1)))

        u = x2 - z1 / z2

        funcU = f(my_counter, u)
        if u < x2:
            if funcU >= func2:
                x1 = u
                func1 = funcU
            else:
                x3 = x2
                func3 = func2
                x2 = u
                func2 = funcU
        else:
            if funcU >= func2:
                x3 = u
                func3 = funcU
            else:
                x1 = x2
                func1 = func2
                x2 = u
                func2 = funcU
    return u, funcU, k, my_counter.get_count()


if __name__ == "__main__":
    print(paraboll_method(A, B, EPSILON))
