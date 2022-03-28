from input import *
from task4 import paraboll_method
from task2 import golden_ratio_method


def brent_method(a, c):
    x = w = v = (a + c) / 2
    fx = fw = fv = f(x)
    d = e = c - a
    u = 0
    while c - a > epsilon:
        print(a, c)
        g, e = e, d
        if len({x, w, v}) == 3 and len({fx, fw, fv}):
            u = paraboll_method(a, c)[1]
        if a - epsilon <= u <= c + epsilon and abs(u - x) < g / 2:
            x1 = a
            x2 = (a + c) / 2
            x3 = c
            func1 = f(x1)
            func2 = f(x2)
            func3 = f(x3)
            u = x2 - ((x2 - x1) ** 2 * (func2 - func3) - (x2 - x3) ** 2 * (func2 - func1)) / (
                    2 * ((x2 - x1) * (func2 - func3) - (x2 - x3) * (func2 - func1)))
            d = abs(u - x)
        else:
            if x < (c - a) / 2:
                u = x + K * (c - x)
                d = c - x
            else:
                u = x - K * (x - a)
                d = x - a
        if abs(u - x) < epsilon:
            u = x + (u - x) * epsilon
        fu = f(u)
        if fu <= fx:
            if u >= x:
                a = x
            else:
                c = x
            v, w, x = w, x, u
            fv, fw, fx = fw, fx, fu
        else:
            if u >= x:
                c = u
            else:
                a = u
            if fu <= fw or w == x:
                u, w = w, u
                fu, fw = fw, fu
            elif fu <= fv or u == x or u == w:
                v = u
                fv = fu
    return a, c, x, w, u, fv


if __name__ == "__main__":
    print(brent_method(A, B))
