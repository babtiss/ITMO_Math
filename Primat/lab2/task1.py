from input import *


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
    draw_save(xn, yn, fn, X, Y, F)

    # по формуле градиентного спуска получаем все значения x y
    while abs(derivative_x(xn, yn) + derivative_y(xn, yn)) > epsilon:
        xn = xn - STEP * derivative_x(xn, yn)
        yn = yn - STEP * derivative_y(xn, yn)
        fn = func(xn, yn)

        count += 1
        draw_save(xn, yn, fn, X, Y, F)

    print(xn, yn, fn, count)
    return X, Y, F


draw_function_plot(gradient_method(func=f_dimensional))
