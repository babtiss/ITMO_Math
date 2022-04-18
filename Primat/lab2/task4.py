from matplotlib import pyplot as plt

from input import *


def _f_x(lambda_, xn, yn):
    return xn - lambda_ * derivative_x(xn, yn)


def _f_y(lambda_, xn, yn):
    return yn - lambda_ * derivative_y(xn, yn)


def fibonacci_method(a, b, n, xn, yn, _f, k=1):
    x1 = a + fib(n - 2) / fib(n) * (b - a)
    x2 = a + fib(n - 1) / fib(n) * (b - a)

    func1, func2 = _f(x1, xn, yn), _f(x2, xn, yn)
    while k != n - 2:
        if func1 > func2:
            a = x1
            x1 = x2
            x2 = a + fib(n - k - 1) / fib(n - k) * (b - a)
            func1 = func2
            func2 = _f(x2, xn, yn)
        else:
            b = x2
            x2 = x1
            x1 = a + fib(n - k - 2) / fib(n - k) * (b - a)
            func2 = func1
            func1 = _f(x1, xn, yn)
        k += 1
    return min(x1, x2)


def gradient_method_fibonacci(func):
    # начальн. значение
    xn = A
    yn = B
    fn = func(xn, yn)
    count = 0

    # заводим словарь, где будем хранить все найденные значения функции
    X = []
    Y = []
    F = []
    X.append(xn)
    Y.append(yn)
    F.append(fn)
    count = 0
    lambda_x = 0
    while func(xn, yn) - func(xn - lambda_x * derivative_x(xn, yn), yn) >= epsilon * lambda_x * derivative_x(xn,
                                                                                                             yn) ** 2:
        # lambda_x = fibonacci_method(0, 0.8, 3, xn, yn, _f_x)
        # lambda_y = fibonacci_method(0, 0.8, 3, xn, yn, _f_y)
        lambda_x = fibonacci_method(0, 1.3, 5, xn, yn, _f_x)
        lambda_y = fibonacci_method(0, 1.3, 5, xn, yn, _f_y)
        count += 1
        xn = xn - lambda_x * derivative_x(xn, yn)
        yn = yn - lambda_y * derivative_y(xn, yn)

        fn = func(xn, yn)

        X.append(xn)
        Y.append(yn)
        F.append(fn)
    print(count, fn)

    return X, Y, F


draw_function_plot(gradient_method_fibonacci(f_dimensional))
