import matplotlib
from matplotlib import pyplot as plt
from scipy.misc import derivative
from input import *


def gradient_method_2(func):
    # начальн. значение
    xn = A
    yn = B
    fn = func(xn, yn)
    count = 0
    stepn = STEP

    # заводим словарь, где будем хранить все найденные значения функции
    X = []
    Y = []
    F = []

    # предыдущие значения xn, yn:
    x_prev = xn
    y_prev = yn
    X.append(xn)
    Y.append(yn)
    F.append(fn)
    count_global = 0
    while abs(derivative_x(xn, yn) + derivative_y(xn, yn)) > epsilon:
        xn, x_prev = x_prev - STEP * derivative_x(x_prev, y_prev), xn
        yn, y_prev = y_prev - STEP * derivative_y(x_prev, y_prev), yn

        fn = func(xn, yn)
        X.append(xn)
        Y.append(yn)
        F.append(fn)
        count_global += 1
        while func(x_prev, y_prev) <= func(xn, yn):
            xn, x_prev = x_prev - STEP * derivative_x(x_prev, y_prev), xn
            yn, y_prev = y_prev - STEP * derivative_y(x_prev, y_prev), yn
            fn = func(xn, yn)
            X.append(xn)
            Y.append(yn)
            F.append(fn)
            stepn = stepn * DELTA
            count += 1
            count_global += 1
            if count == 100:
                stepn = STEP
                count = 0
        print(count_global)

    return X, Y, F


draw_function_plot(gradient_method_2(f_dimensional))
