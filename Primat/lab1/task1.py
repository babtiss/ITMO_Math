from lab1.input import *


def dichotomy_method(a, b, c=0):
    while b - a > epsilon:
        c += 1
        middle = (a + b) / 2
        x1 = middle - delta
        x2 = middle + delta
        if f(x2) > f(x1):
            a, b = a, x2
        else:
            a, b = x1, b
    return [a, f((a + b) / 2), b, c]


if __name__ == "__main__":
    print(dichotomy_method(A, B))
