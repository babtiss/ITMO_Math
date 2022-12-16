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
        [7, 1],
        [2, 11]
    ])
    main(matrix)
    print("_" * 100)
    simplex = Simplex.read_from_file(f'./input-files/task8.txt')
    solve = simplex.solve()
    solution = simplex.get_solution()
    print("solve", solve)
    print("solution", solution)
    print("_" * 100)
    print("Оптимальное решение в смешанной стратегии: ", [solution[i] / solve for i in range(len(solution[:-2]))])
    print("Цена игры", 1 / solve)


