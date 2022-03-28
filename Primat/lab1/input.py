import math

epsilon = 10 ** (-5)
delta = 10 ** (-6)
A, B = 2, 7
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


my_counter = Counter()


def f(x: float) -> float:
    global my_counter
    my_counter.plus()
    return math.e ** (math.sin(x) * math.log(x, math.e))


def fib(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)