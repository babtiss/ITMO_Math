import matplotlib.pyplot as plt

from input import *
from task1 import dichotomy_method
from task2 import golden_ratio_method
from task3 import fibonacci_method
from task4 import paraboll_method
from task5 import brent_method


def graph(x, y, method):
    plt.figure(figsize=(9, 9))
    plt.subplot(2, 1, 1)
    plt.plot(
        ["10ˆ(-1)", "10ˆ(-2)", "10ˆ(-3)", "10ˆ(-4)", "10ˆ(-5)", "10ˆ(-6)", "10ˆ(-7)", "10ˆ(-8)"],
        y)
    plt.title(f"{method}: f_invocations(epsilon)")
    plt.xlabel("epsilon", fontsize=14)
    plt.ylabel("f_invocations", fontsize=14)
    plt.grid(True)
    plt.show()


def t1():
    x = [10 ** (-i) for i in range(1, 9)]
    y = [dichotomy_method(A, B, epsilon)[3] for epsilon in x]
    graph(x, y, "dichotomy_method")


def t2():
    x = [10 ** (-i) for i in range(1, 9)]
    y = [golden_ratio_method(A, B, epsilon)[3] for epsilon in x]
    graph(x, y, "golden_ratio_method")


def t3():
    x = [10 ** (-i) for i in range(1, 9)]
    y = [fibonacci_method(A, B, N, epsilon)[3] for epsilon in x]
    graph(x, y, "fibonacci_method")


def t4():
    x = [10 ** (-i) for i in range(3, 11)]
    y = [paraboll_method(A, B, epsilon)[3] for epsilon in x]
    graph(x, y, "paraboll_method")


def t5():
    x = [10 ** (-i) for i in range(1, 9)]
    y = [brent_method(A, B, epsilon)[3] for epsilon in x]
    graph(x, y, "brent_method")


if __name__ == "__main__":
    t2()
