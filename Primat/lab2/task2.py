from input import *


def gradient_method_2(func):
    # начальн. значение
    xn = A
    yn = B
    fn = func(xn, yn)
    count = 0
    stepn = STEP
    x_prev = xn
    y_prev = yn

    # заводим словарь, где будем хранить все найденные значения функции
    X = []
    Y = []
    F = []
    draw_save(xn, yn, fn, X, Y, F)

    # по формуле градиентного спуска получаем все значения x y
    while abs(derivative_x(xn, yn) + derivative_y(xn, yn)) > epsilon:
        xn, x_prev = x_prev - STEP * derivative_x(x_prev, y_prev), xn
        yn, y_prev = y_prev - STEP * derivative_y(x_prev, y_prev), yn

        fn = func(xn, yn)
        draw_save(xn, yn, fn, X, Y, F)

        # дробление STEP
        while func(x_prev, y_prev) <= func(xn, yn):
            xn, x_prev = x_prev - STEP * derivative_x(x_prev, y_prev), xn
            yn, y_prev = y_prev - STEP * derivative_y(x_prev, y_prev), yn

            fn = func(xn, yn)

            draw_save(xn, yn, fn, X, Y, F)

            stepn = stepn * DELTA
            count += 1

            # Каждые 100 итераций сбрасываем шаг до начального
            if count % 100 == 0:
                stepn = STEP

    print(xn, yn, fn, count)

    return X, Y, F


draw_function_plot(gradient_method_2(f_dimensional))
