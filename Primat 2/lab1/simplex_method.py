import sys
import numpy as np


class Simplex:
    eps = 1 / 10**8

    def __init__(self, table=None, basis=None, source=None, point=None):
        if table is not None and basis is not None:
            self.n = len(table)
            self.m = len(table[0])
            self.num_arg = self.m - 1
            self.table = table
            self.basis = basis

        elif source is not None and basis is not None:
            self.n = len(source)
            self.m = len(source[0])
            self.num_arg = self.m - 1

            self.get_first_plan(source, basis)

            print("First plan:")
            self.print_table()

        elif source is not None and point is not None:
            self.n = len(source)
            self.m = len(source[0])
            self.num_arg = self.m - 1

            basis = []
            for i in range(len(point)):
                if point[i] != 0:
                    basis.append(i + 1)

            self.get_first_plan(source, basis)

            print("First plan:")
            self.print_table()

        elif source is not None:
            self.n = len(source)
            self.m = len(source[0])
            self.num_arg = self.m - 1
            opt_func = source[self.n - 1]

            print("Creating table with synthetic basis:")
            self.create_table_with_synthetic_basis(source)

            self.calculate()

            all_null = True
            for j in range(self.m - self.n + 1):
                if self.table[self.n - 1][j] > Simplex.eps:
                    all_null = False
                    break
            if not all_null:
                print(
                    "В результате получения первого опорного плана не все искусственные переменные равны нулю. "
                    "Решений нет!")
                sys.exit()

            new_table = [[0] * (self.m - self.n + 1) for i in range(self.n)]
            for i in range(len(new_table)):
                for j in range(len(new_table[0])):
                    new_table[i][j] = self.table[i][j]

            for j in range(len(new_table[0])):
                sum_col = 0
                for i in range(len(new_table) - 1):
                    sum_col += new_table[i][j] * opt_func[self.basis[i]]
                new_table[len(new_table) - 1][j] = sum_col - opt_func[j]
            new_table[len(new_table) - 1] = list(np.array(new_table[len(new_table) - 1]) * (-1))

            self.table = new_table
            self.n = len(self.table)
            self.m = len(self.table[0])

            print("\nCreated first plan:")
            self.print_table()

        else:
            print("No data!")
            sys.exit()

    def calculate(self):
        print("First table:")
        self.print_table()

        while not self.is_end():
            main_col = self.find_main_col()
            main_row = self.find_main_row(main_col)

            if main_row == -1:
                print(
                    "Не удалось выбрать опорный элемент. Задача не имеет решений, так как ОДР не ограничена")
                sys.exit()

            print("Pivot element: (" + str(main_row + 1) + ";" + str(main_col + 1) + ")")

            self.basis[main_row] = main_col

            self.make_step(main_row, main_col)
            self.print_table()

        result = [0 for i in range(self.num_arg)]
        for i in range(len(self.basis)):
            if self.basis[i] <= self.num_arg:
                result[self.basis[i] - 1] = self.table[i][0]
        print("Result:")
        print(result)

        return [self.table, result]

    def is_end(self):
        flag = True
        for j in range(1, self.m):
            if self.table[self.n - 1][j] < -Simplex.eps:
                flag = False
                break
        return flag

    def find_main_col(self):
        main_col = 1
        for j in range(2, self.m):
            if self.table[self.n - 1][j] < self.table[self.n - 1][main_col]:
                main_col = j
        return main_col

    def find_main_row(self, main_col):
        main_row = -1
        for i in range(self.n - 1):
            if self.table[i][main_col] > Simplex.eps:
                main_row = i
                break

        if main_row == -1:
            return -1

        for i in range(main_row + 1, self.n - 1):
            if (self.table[i][main_col] > Simplex.eps) and (
                    self.table[i][0] / self.table[i][main_col] <
                    self.table[main_row][0] / self.table[main_row][main_col]):
                main_row = i

        return main_row

    def make_step(self, main_row, main_col):
        new_table = [[0] * self.m for i in range(self.n)]

        for j in range(self.m):
            new_table[main_row][j] = self.table[main_row][j] / self.table[main_row][main_col]

        for i in range(self.n):
            if i == main_row:
                continue

            for j in range(self.m):
                new_table[i][j] = self.table[i][j] - (self.table[main_row][j] / self.table[main_row][main_col]) * \
                                  self.table[i][main_col]
                new_table[i][j] = new_table[i][j]

        self.table = new_table

    def get_first_plan(self, source, basis):
        print("Try to get first plan:")
        self.table = source
        self.basis = [-1 for i in range(len(basis))]
        for basis_arg in basis:
            main_col = basis_arg
            main_row = -1
            for i in range(self.n - 1):
                if self.basis[i] == -1 and self.table[i][main_col] > Simplex.eps:
                    main_row = i

            if main_row == -1:
                print("Невозможно ввести базисные перменные в базис")
                sys.exit()

            print("Pivot element: (" + str(main_row + 1) + ";" + str(main_col + 1) + ")")

            self.basis[main_row] = main_col

            self.make_step(main_row, main_col)
            self.print_table()

    def print_table(self):
        print()
        for i in range(len(self.table)):
            print(self.table[i])
        print()

    def create_table_with_synthetic_basis(self, source):
        self.basis = list()
        self.table = [[0] * (self.m + self.n - 1) for i in range(self.n)]

        # create first table
        for i in range(self.n):
            for j in range(len(self.table[0])):
                if j < self.m:
                    self.table[i][j] = source[i][j]
                else:
                    self.table[i][j] = 0

            # add basis
            if (self.m + i) < len(self.table[0]):
                self.table[i][self.m + i] = 1
                self.basis.append(self.m + i)

        self.m = len(self.table[0])

        for j in range(self.m):
            sum = 0
            for i in range(self.n - 1):
                sum -= self.table[i][j]
            self.table[self.n - 1][j] = sum
        for basis_col in self.basis:
            self.table[self.n - 1][basis_col] = 0


class LinearProgrammingTask:
    def __init__(self, f, restrictions, max_min, start_point=None):

        self.func_coef = list(f)
        for i in range(len(f) - 1, 0, -1):
            f[i], f[i - 1] = f[i - 1], f[i]
        # reversing
        if max_min == "max":
            f = np.array(f) * (-1)

        table = [[0] * (len(restrictions[0]) - 1) for i in range(len(restrictions) + 1)]
        table[len(restrictions)] = list(f)
        for i in range(len(restrictions)):
            for j in range(len(restrictions[0])):
                if j < len(restrictions[0]) - 2:
                    table[i][j + 1] = restrictions[i][j]
                elif j == len(restrictions[0]) - 2:
                    table[i][0] = restrictions[i][j + 1]

        # change '>=' to '<='
        for i in range(len(restrictions)):
            if restrictions[i][len(restrictions[0]) - 2] == ">=":
                table[i] = list(np.array(table[i]) * (-1))

        # change '<=' to '='
        for i in range(len(restrictions)):
            if restrictions[i][len(restrictions[0]) - 2] != "=":
                restrictions = np.array(restrictions)
                table = np.array(table)
                new_column = np.zeros(len(restrictions) + 1)
                new_column[i] = 1
                table = np.column_stack((table, new_column))

        # change b to positive
        for i in range(len(table)):
            if table[i][0] < 0:
                table[i] = list(np.array(table[i]) * (-1))
        self.table = table
        self.f = f
        self.start_point = start_point

    def solve(self):
        if self.start_point is None:
            simplex = Simplex(source=self.table)
            result_table, result = simplex.calculate()
        else:
            simplex = Simplex(source=self.table, point=self.start_point)
            result_table, result = simplex.calculate()
        end_result = []
        result_f = 0
        for i in range(len(self.func_coef) - 1):
            end_result.append(round(result[i], 4))
            result_f += self.func_coef[i] * end_result[i]
        print("___________")
        print("RESULT:")
        print(end_result)
        print("f= " + str(result_f))