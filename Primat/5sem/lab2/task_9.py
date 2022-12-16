import numpy as np

from task_1 import *
from task_2 import *


def main(matrix):
    pure = is_pure(matrix)
    if pure[0]:
        print("Чистая стратегия применима, седловая точка:", pure[1], pure[2])
        print("Цена игры = ", pure[3])
        print("Матожидание = ", pure[3])
    else:
        print("Чистая стратегия не применима")
        print("решите злп для матрицы:", matrix)


if __name__ == "__main__":


    matrix = numpy.array([
        [2, 5, 1],
        [3, 4, 4],
        [2, 1, 6]
    ])
    main(matrix)

