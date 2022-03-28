import math

from lab1.input import epsilon, A, B


def f(x):
    return math.e ** (math.log(x, math.e) * math.sin(x))


def paraboll_method(a, b, k=1):
    x1 = a
    x2 = (a + b) / 2
    x3 = b

    func1 = f(x1)
    func2 = f(x2)
    func3 = f(x3)
    funcU = 0
    while x3 - x1 >= epsilon:
        k += 1
        u = x2 - ((x2 - x1) ** 2 * (func2 - func3) - (x2 - x3) ** 2 * (func2 - func1)) / (
                2 * ((x2 - x1) * (func2 - func3) - (x2 - x3) * (func2 - func1)))
        funcU = f(u)
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
    return funcU, u, k


if __name__ == "__main__":
    print(paraboll_method(A, B))
