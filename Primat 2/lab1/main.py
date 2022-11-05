import simplex_method

# Формат данных следующий:
# Первый столбец - столбец свободных членов
# Последняя строка - целевая функция

# Task1
input_source_1 = [[4, 3, 1, -1, 1],
                  [4, 5, 1, 1, -1],
                  [0, -6, -1, -4, 5]]
point_1 = [1, 0, 0, 1]

task1 = simplex_method.LinearProgrammingTask(
    start_point=point_1,

    f=[-6, -1, -4, 5, 0],
    restrictions=[[3, 1, -1, 1, "=", 4],
                  [5, 1, 1, -1, "=", 4]],
    max_min="min")

# Task2
input_source_2 = [[-4, 1, -3, -1, -2],
                  [0, 1, -1, 1, 0],
                  [0, -1, -2, -3, 1]]
point_2 = [0, 1, 1, 0]

task2 = simplex_method.LinearProgrammingTask(
    start_point=point_2,

    f=[-1, -2, -3, 1, 0],
    restrictions=[[1, -3, -1, -2, "=", -4],
                  [1, -1, 1, 0, "=", 0]],
    max_min="min")

# Task3
input_source_3 = [[5, 1, 1, 0, 2, 1],
                  [9, 1, 1, 1, 3, 2],
                  [6, 0, 1, 1, 2, 1],
                  [0, -1, -2, -1, 3, -1]]
point_3 = [1, 2, 1, 0, 0]

task3 = simplex_method.LinearProgrammingTask(
    start_point=point_3,
    f=[-1, -2, -1, 3, -1, 0],
    restrictions=[[1, 1, 0, 2, 1, "=", 5],
                  [1, 1, 1, 3, 2, "=", 9],
                  [0, 1, 1, 2, 1, "=", 6],


                  ],
    max_min="min")

# Task4
input_source_4 = [[4, 1, 1, 2, 0, 0],
                  [-6, 0, -2, -2, 1, -1],
                  [12, 1, -1, 6, 1, 1],
                  [0, -1, -1, -1, 1, -1]]
point_4 = [1, 1, 2, 0, 0]

task4 = simplex_method.LinearProgrammingTask(
    f=[-1, -1, -1, 1, -1, 0],
    restrictions=[[1, 1, 2, 0, 0, "=", 4],
                  [0, -2, -2, 1, -1, "=", -6],
                  [1, -1, 6, 1, 1, "=", 12]],
    max_min="min")

# Task5
input_source_5 = [[0, 1, 1, -1, -10],
                  [11, 1, 14, 10, -10],
                  [0, -1, 4, -3, 10]]

task5 = simplex_method.LinearProgrammingTask(

    f=[-1, 4, -3, 10, 0],
    restrictions=[[1, 1, -1, -10, "=", 0],
                  [1, 14, 10, -10, "=", 11]],
    max_min="min"
)

# Task6
input_table_6 = [[3, 1, 3, 3, 1, 1, 0],
                 [4, 2, 0, 3, -1, 0, 1],
                 [0, -1, 5, 1, -1, 0, 0]]
basis_6 = [5, 6]

task6 = simplex_method.LinearProgrammingTask(
    f=[-1, 5, 1, -1, 0],
    restrictions=[[1, 3, 3, 1, "<=", 3],
                  [2, 0, 3, -1, "<=", 4]],
    max_min="min"
)

task7 = simplex_method.LinearProgrammingTask(
    f=[-1, -1, 1, -1, 2, 0],
    restrictions=[[3, 1, 1, 1, -2, "=", 10],
                  [6, 1, 2, 3, -4, "=", 20],
                  [10, 1, 3, 6, -7, "=", 30]],
    max_min="min"
)

# Task7
input_source_7 = [[10, 3, 1, 1, 1, -2],
                  [20, 6, 1, 2, 3, -4],
                  [30, 10, 1, 3, 6, -7],
                  [0, -1, -1, 1, -1, 2]]

input_source_8 = [[30, 3, 5, 1, 0, 0],
                  [12, 4, -3, 0, 1, 0],
                  [-6, -1, 3, 0, 0, 1],
                  [0, -1, -1, 0, 0, 0]]

task8 = simplex_method.LinearProgrammingTask(
    f=[1, 1, 0],
    restrictions=[[3, 5, "<=", 30],
                  [4, -3, "<=", 12],
                  [1, -3, ">=", 6]],
    max_min="max")

input_source_9 = [[4, 1, 2, 1, 0, 0],
                  [1, 1, -1, 0, 1, 0],
                  [8, 1, 1, 0, 0, 1],
                  [0, 1, -3, 0, 0, 0]]
basis_9 = [3, 4, 5]

myself_task1 = simplex_method.LinearProgrammingTask(
    f=[1, 5, -2, 1, 0],
    restrictions=[[1, 2, 1, -4, "<=", 4],
                  [2, 0, 3, 0, ">=", -1],
                  [1, 5, 1, 3, "=", 11]],
    max_min="max"
)

myself_task2 = simplex_method.LinearProgrammingTask(
    f=[1, -1, 1, 0],
    restrictions=[[1, 2, 3, ">=", 4],
                  [2, 3, 4, ">=", 3]],
    max_min="max"
)

# Пример использования класса Simplex
# simplex = simplex_method.Simplex(source=input_source_1)
# simplex.calculate()

test_task = simplex_method.LinearProgrammingTask(
    f=[1, 1, 0],
    restrictions=[[3, 5, "<=", 30],
                  [4, -3, "<=", 12],
                  [1, -3, ">=", 6]],
    max_min="max"
)

lab2_task2 = simplex_method.LinearProgrammingTask(
    f=[8, 7, 12, 13, 0],
    restrictions=[[1, 0, 1, 0, "=", 230],
                  [0, 1, 0, 1, "=", 68],
                  [1 / 10, 1 / 12, 0, 0, "<=", 24],
                  [0, 0, 1 / 13, 1 / 13, "<=", 24]],
    max_min="min"
)

lab2_task3 = simplex_method.LinearProgrammingTask(
    f=[12, 8, 0],
    restrictions=[[40, 10, ">=", 1000],
                  [1.25, 2.5, ">=", 100],
                  [2, 1, ">=", 80],
                  [1, 1, ">=", 60]],
    max_min="min"
)

lab2_task4_1 = simplex_method.LinearProgrammingTask(
    f=[1, 1, 0],
    restrictions=[[4, 2, ">=", 1],
                  [2, 3, ">=", 1]],
    max_min="min"
)

lab2_task4_2 = simplex_method.LinearProgrammingTask(
    f=[1, 1, 0],
    restrictions=[[4, 2, "<=", 1],
                  [2, 3, "<=", 1]],
    max_min="max"
)

lab2_task5 = simplex_method.LinearProgrammingTask(
    f=[1, 1, 0],
    restrictions=[[8, 4, ">=", 1],
                  [4, 8, ">=", 1],
                  [6, 5, ">=", 1]],
    max_min="min"
)

lab2_task6_1 = simplex_method.LinearProgrammingTask(
    f=[1, 1, 1, 1, 0],
    restrictions=[[7, 2, 5, 3, ">=", 1],
                  [2, 2, 3, 2, ">=", 1],
                  [5, 3, 4, 1, ">=", 1],
                  [1, 4, 4, 6, ">=", 1]],
    max_min="min"
)

lab2_task6_2 = simplex_method.LinearProgrammingTask(
    f=[1, 1, 1, 1, 0],
    restrictions=[[7, 2, 5, 1, "<=", 1],
                  [2, 2, 3, 4, "<=", 1],
                  [5, 3, 4, 4, "<=", 1],
                  [3, 2, 1, 6, "<=", 1]],
    max_min="max"
)

lab2_task8 = simplex_method.LinearProgrammingTask(
    f=[1, 1, 0],
    restrictions=[[7, 2, ">=", 1],
                  [1, 11, ">=", 1]],
    max_min="min"
)



# task1.solve()
# task2.solve()

task3.solve()
# task4.solve()
#
# task5.solve()
# task6.solve()
#
# task7.solve()
