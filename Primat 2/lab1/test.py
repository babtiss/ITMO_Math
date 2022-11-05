import simplex as simplex_method


# Формат данных следующий:
# Первый столбец - столбец свободных членов
# Последняя строка - целевая функция

# Task1
def task1():
    point_1 = [1, 0, 0, 1]

    task1 = simplex_method.LinearProgrammingTask(
        f=[-6, -1, -4, 5, 0],
        start_point=point_1,
        restrictions=[[3, 1, -1, 1, "=", 4],
                      [5, 1, 1, -1, "=", 4]],
        max_min="min")
    # task1.solve()
    return


def a():

    point_2 = [0, 1, 1, 0]

    task2 = simplex_method.LinearProgrammingTask(
        start_point=point_2,
        f=[-1, -2, -3, 1, 0],
        restrictions=[[1, -3, -1, -2, "=", -4],
                      [1, -1, 1, 0, "=", 0]],
        max_min="min")

    point_3 = [0, 0, 1, 2, 1]

    task3 = simplex_method.LinearProgrammingTask(
        start_point=point_3,
        f=[-1, -2, -1, 3, -1, 0],
        restrictions=[[1, 1, 0, 2, 1, "=", 5],
                      [1, 1, 1, 3, 2, "=", 9],
                      [0, 1, 1, 2, 1, "=", 6]],
        max_min="min")

    point_4 = [1, 1, 2, 0, 0]

    task4 = simplex_method.LinearProgrammingTask(
        f=[-1, -1, -1, 1, -1, 0],
        start_point=point_4,
        restrictions=[[1, 1, 2, 0, 0, "=", 4],
                      [0, -2, -2, 1, -1, "=", -6],
                      [1, -1, 6, 1, 1, "=", 12]],
        max_min="min")


    task5 = simplex_method.LinearProgrammingTask(
        f=[-1, 4, -3, 10, 0],
        restrictions=[[1, 1, -1, -10, "=", 0],
                      [1, 14, 10, -10, "=", 11]],
        max_min="min"
    )

    task6 = simplex_method.LinearProgrammingTask(
        f=[-1, 5, 1, -1, 0],
        restrictions=[[1, 3, 3, 1, "<=", 3],
                      [2, 0, 3, -1, "<=", 4]],
        max_min="min"
    )

    task7 = simplex_method.LinearProgrammingTask(
        f=[-1, -1, 1, -1, 2, 0],
        start_point=[5, 6],
        restrictions=[[3, 1, 1, 1, -2, "=", 10],
                      [6, 1, 2, 3, -4, "=", 20],
                      [10, 1, 3, 6, -7, "=", 30]],
        max_min="min"
    )
