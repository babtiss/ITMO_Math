from input import *


def _golden_selection(a, b, xn, yn, px, py, _f):
    k1 = K1
    k2 = K2

    lambda1 = a + k1 * (b - a)
    lambda2 = a + k2 * (b - a)

    while abs(b - a) > 2 * 0.4:
        xn = xn + lambda1 * px
        yn = yn + lambda1 * py
        xn_ = xn + lambda2 * px
        yn_ = yn + lambda2 * py
        f1 = _f(xn, yn)
        f2 = _f(xn_, yn_)
        if f1 < f2:
            b = lambda2
            lambda2 = lambda1
            lambda1 = a + k1 * (b - a)
            xn = xn + lambda1 * px
            yn = yn + lambda1 * py
        else:
            a = lambda1
            lambda1 = lambda2
            lambda2 = a + k2 * (b - a)
    return (a + b) / 2


def _f_x(lambda_, xn, yn):
    return xn + lambda_ * derivative_x(xn, yn)


def _f_y(lambda_, xn, yn):
    return yn + lambda_ * derivative_y(xn, yn)


def fletcher_reeves_method(func):
    # начальн. значение
    xn = A
    yn = B
    fn = func(xn, yn)
    count = 0
    grad_x = -derivative_x(xn, yn)
    grad_y = -derivative_y(xn, yn)
    grad_square = grad_x ** 2 + grad_y ** 2

    # заводим словарь, где будем хранить все найденные значения функции
    X = []
    Y = []
    F = []
    draw_save(xn, yn, fn, X, Y, F)

    # по формуле градиентного спуска получаем все значения x y
    while grad_square > epsilon:
        count += 1

        # методом золотого сечения находим оптимальный lambda
        lambda_ = _golden_selection(0, 0.5, xn, yn, grad_x, grad_y, func)
        xn = xn + lambda_ * grad_x
        yn = yn + lambda_ * grad_y

        grad_new_x = -derivative_x(xn, yn)
        grad_new_y = -derivative_y(xn, yn)
        grad_new_square = grad_new_x ** 2 + grad_new_y ** 2

        # сбрасываем betta каждые 10 итераций
        if count % 10 == 0:
            beta = 0
        else:
            beta = grad_new_square / grad_square

        grad_x = grad_new_x + beta * grad_x
        grad_y = grad_new_y + beta * grad_y
        grad_square = grad_x ** 2 + grad_y ** 2

        fn = func(xn, yn)

        draw_save(xn, yn, fn, X, Y, F)
        print(fn, xn, yn)

    print(count)
    return X, Y, F


draw_function_plot(fletcher_reeves_method(func=f_dimensional))
