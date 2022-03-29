import math

EPSILON = 10 ** (-15)
delta = 10 ** (-11)
A, B = 3, 7
GOLD = 2 / (1 + math.sqrt(5))
N = 14
K = (3 - math.sqrt(5)) / 2


class Counter:
    def __init__(self):
        self.count = 0

    def plus(self):
        self.count += 1

    def get_count(self):
        return self.count


def f(my_counter: Counter, x: float) -> float:
    my_counter.plus()
    return round(math.e ** (math.sin(x) * math.log(x, math.e)), 32)


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
