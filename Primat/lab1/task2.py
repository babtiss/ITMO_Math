from input import *


def golden_ratio_method(a, b, epsilon, k=1):
    x2 = a + GOLD * (b - a)
    x1 = b - GOLD * (b - a)
    my_counter = Counter()
    func1, func2 = f(my_counter, x1), f(my_counter, x2)
    while b - a > 2 * epsilon:
        k += 1
        if func1 >= func2:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
            func1, func2 = func2, f(my_counter, x2)
        else:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
            func1, func2 = f(my_counter, x1), func1

    return (a + b) / 2, f(Counter(), (a + b) / 2), k, my_counter.get_count()


if __name__ == "__main__":
    print(golden_ratio_method(A, B, EPSILON))
