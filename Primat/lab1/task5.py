from input import *
from task4 import paraboll_method


def brent_method(a, c, epsilon):
    x = w = v = (a + c) / 2
    my_counter = Counter()
    fx = fw = fv = f(my_counter, x)
    d = e = c - a
    u = 0
    k = 1

    while c - a > epsilon:

        k += 1
        g, e = e, d

        if len({x, w, v}) == 3 and len({fx, fw, fv}) == 3 and a + epsilon <= u <= c - epsilon and abs(u - x) < g / 2:

            x1 = x
            x2 = v
            x3 = w
            func1 = fx
            func2 = fv
            func3 = fw
            z1 = (x2 - x1) ** 2 * (func2 - func3) - (x2 - x3) ** 2 * (func2 - func1)
            z2 = (2 * ((x2 - x1) * (func2 - func3) - (x2 - x3) * (func2 - func1)))

            u = x2 - z1 / z2

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
            return u, fv, k, my_counter.get_count()
        fu = f(my_counter, u)
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
                v, w = w, u
                fv, fw = fw, fu
            elif fu <= fv or v == x or v == w:
                v = u
                fv = fu
    return u, fv, k, my_counter.get_count()


if __name__ == "__main__":
    print(brent_method(A, B, EPSILON))
