from matplotlib import pyplot as plt
from input import *


# подготовка к Град. спуску


def gradient_method(func):
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
    # по формуле градиентного спуска получаем все значения x y
    while abs(derivative_x(xn, yn) + derivative_y(xn, yn)) > epsilon:
        xn = xn - STEP * derivative_x(xn, yn)
        yn = yn - STEP * derivative_y(xn, yn)

        count += 1

        fn = func(xn, yn)
        X.append(xn)
        Y.append(yn)
        F.append(fn)
    print(xn, yn)
    return X, Y, F


draw_function_plot(gradient_method(func=f_dimensional))