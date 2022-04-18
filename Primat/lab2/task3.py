from matplotlib import pyplot as plt

from input import *


def _golden_selection(a, b, xn, yn, eps, _f):
    k1 = (3 - math.sqrt(5)) / 2
    k2 = (math.sqrt(5) - 1) / 2

    lambda1 = a + k1 * (b - a)
    lambda2 = a + k2 * (b - a)
    f1 = _f(lambda1, xn, yn)
    f2 = _f(lambda2, xn, yn)
    while b - a > 2 * eps:
        if f1 < f2:
            b = lambda2
            lambda2 = lambda1
            f2 = f1
            lambda1 = a + k1 * (b - a)
            f1 = _f(lambda1, xn, yn)
        else:
            a = lambda1
            lambda1 = lambda2
            f1 = f2
            lambda2 = a + k2 * (b - a)
            f2 = _f(lambda2, xn, yn)
    return (a + b) / 2


def _f_x(lambda_, xn, yn):
    return xn - lambda_ * derivative_x(xn, yn)


def _f_y(lambda_, xn, yn):
    return yn - lambda_ * derivative_y(xn, yn)


def gradient_method_golden(func):
    # начальн. значение
    xn = A
    yn = B
    fn = func(xn, yn)
    X = []
    Y = []
    F = []
    # заводим словарь, где будем хранить все найденные значения функции
    X.append(xn)
    Y.append(yn)
    F.append(fn)
    count = 0
    lambda_x = 0

    while func(xn, yn) - func(xn - lambda_x * derivative_x(xn, yn), yn) >= epsilon * lambda_x * derivative_x(xn,
                                                                                                             yn) ** 2:
        count += 1
        # lambda_x = _golden_selection(0, 0.8, xn, yn, 0.4, _f_x)
        # lambda_y = _golden_selection(0, 0.8, xn, yn, 0.4, _f_y)
        lambda_x = _golden_selection(0, 1.9, xn, yn, 2, _f_x)
        lambda_y = _golden_selection(0, 1.9, xn, yn, 2, _f_y)
        xn = xn - lambda_x * derivative_x(xn, yn)
        yn = yn - lambda_y * derivative_y(xn, yn)
        fn = func(xn, yn)
        X.append(xn)
        Y.append(yn)
        F.append(fn)

    print(count, fn)
    return X, Y, F


draw_function_plot(gradient_method_golden(f_dimensional))
