from input import *


def golden_ratio_method(a, b, c=0):
    x2 = a + GOLD * (b - a)
    x1 = b - GOLD * (b - a)
    func1, func2 = f(x1), f(x2)
    while b - a > 2 * epsilon:
        c += 1
        if func1 > func2:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            func1, func2 = func2, f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            func1, func2 = f(x1), func1

    return a, b, f((a + b) / 2), c


if __name__ == "__main__":
    print(golden_ratio_method(A, B))
