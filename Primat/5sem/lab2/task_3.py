from task_2 import *


if __name__ == '__main__':
    task_num = 3
    simplex = Simplex.read_from_file(f'./input-files/task{task_num}.txt')
    print(simplex.solve())
    print(simplex.get_solution())
    print("_" * 100)
