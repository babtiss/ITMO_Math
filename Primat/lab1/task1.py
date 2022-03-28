from input import *


def dichotomy_method(a, b, epsilon, k=1):
    while b - a > epsilon:
        k += 1
        middle = (a + b) / 2
        x1 = middle - delta
        x2 = middle + delta
        if f(x2) > f(x1):
            a, b = a, x2
        else:
            a, b = x1, b
    return (a + b) / 2, f((a + b) / 2), k, my_counter.get_count()


if __name__ == "__main__":
    print(dichotomy_method(A, B, EPSILON))
