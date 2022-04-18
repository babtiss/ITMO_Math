import math
import numpy as np
from matplotlib import pyplot as plt


# Производные по аргументам
def derivative_y(x, y):
    return (f_dimensional(x, y + derivative_epsilon) -

            f_dimensional(x, y)) / derivative_epsilon


def derivative_x(x, y):
    return (f_dimensional(derivative_epsilon + x, y) -

            f_dimensional(x, y)) / derivative_epsilon


def fib(n):
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2


def get_grid(grid_step, radius):
    samples = np.arange(-radius, radius, grid_step)
    x, y = np.meshgrid(samples, samples)
    return x, y, f_dimensional(x, y)


def draw_save(x, y, f, X, Y, F):
    X.append(x)
    Y.append(y)
    F.append(f)


def draw_function_plot(points):
    grid_x, grid_y, grid_z = get_grid(0.05, 8)

    X, Y, F = points[0], points[1], points[2]
    print(grid_x, grid_y, grid_z)
    plt.rcParams.update({
        'figure.figsize': (8, 8),
        'figure.dpi': 200,
        'xtick.labelsize': 8,
        'ytick.labelsize': 8
    })

    ax = plt.figure().add_subplot(111, projection='3d')
    ax.plot(X[0:len(X) - 1], Y[0:len(X) - 1], F[0:len(X) - 1], "-o", color="red", markersize=6)
    ax.scatter(X[len(X) - 1], Y[len(X) - 1], F[len(X) - 1], color="white")
    ax.plot_surface(grid_x, grid_y, grid_z, rstride=5, cstride=5, alpha=0.7)
    plt.show()


# 1 Функция
def f_dimensional(x, y):
    return x ** 2 + y ** 2


# CONST
K1 = (3 - math.sqrt(5)) / 2
K2 = (math.sqrt(5) - 1) / 2

# Границы поиска 1 функции
A = -6
B = 7
STEP = 0.1
derivative_epsilon = 0.000001
epsilon = 0.00001
DELTA = 0.5

# # 2 Функция
# def f_dimensional(x, y):
#     return x ** 2 + 2 * y ** 2 - 3 * x + 5 * y - x * y
#
#
# # Границы поиска 2 функции
# A = -4
# B = 4
# STEP = 0.1
# derivative_epsilon = 0.000001
# epsilon = 0.00001
# DELTA = 0.5
