from input import *


def dichotomy_method(a, b, epsilon, k=1):
    my_counter = Counter()
    while b - a > epsilon:
        k += 1
        middle = (a + b) / 2
        x1 = middle - delta
        x2 = middle + delta
        if f(my_counter, x2) > f(my_counter, x1):
            a, b = a, x2
        else:
            a, b = x1, b
    return (a + b) / 2, f(Counter(), (a + b) / 2), k, my_counter.get_count()


if __name__ == "__main__":
    print(dichotomy_method(A, B, EPSILON))
