from input import *


def fibonacci_method(a, b, n, k=1):
    x1 = a + fib(n - 2) / fib(n) * (b - a)
    x2 = a + fib(n - 1) / fib(n) * (b - a)
    func1, func2 = f(x1), f(x2)
    while k != n - 2:
        if func1 > func2:
            a = x1
            x1 = x2
            x2 = a + fib(n - k - 1) / fib(n - k) * (b - a)
            func1 = func2
            func2 = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = a + fib(n - k - 2) / fib(n - k) * (b - a)
            func2 = func1
            func1 = f(x1)
        k += 1
    return min(x1, x2), min(func1, func2), k, my_counter.get_count()


if __name__ == "__main__":
    print(fibonacci_method(A, B, N))
