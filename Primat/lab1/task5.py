from input import *
from lab1.task4 import paraboll_method
from task2 import golden_ratio_method


def brent_method(a, c):
    x, w, v = (a + c) / 2
    fx, fw, fv = f(x)
    d, e = c - a
    while c - a > epsilon:
        g, e = e, d
        if len({x, w, v}) == 3 and len({fx, fw, fv}):
            u = paraboll_method()       # тут
        if a + epsilon <= u <= c - epsilon and u - x < g / 2:
            # u - подходит
            d = abs(u - x)
        else:
            if x < (c - a) / 2:
                u = x + golden_ratio_method(x, c)
                d = c - x
            else:
                u = x - golden_ratio_method(a, x)
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


if __name__ == "__main__":
    print(brent_method(A, B))
