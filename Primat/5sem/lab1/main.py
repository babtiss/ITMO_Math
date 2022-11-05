from __future__ import annotations
import numpy as np
import math
import itertools


class Simplex:
    """Simplex Method class"""
    a: np.array
    b: np.array
    c: np.array
    is_max: bool
    tableau: np.array

    def __init__(
            self,
            a: np.array,
            b: np.array,
            c: np.array,
            is_max: bool,
    ):
        self.a = a
        self.b = b
        self.c = c
        self.ans = 0
        self.is_max = is_max
        self.to_tableau()
        self.make_basic_columns()
        self.fix_b()

    def fix_b(self):
        """Check if any b is < 0 and fix it"""
        if any(x < 0 for x in self.b):
            row_index = np.argmin(self.b)
            column_index = np.argmin(self.a[row_index])
            self.next_step(row_index, column_index)

    def make_basic_columns(self):
        columns = np.array(self.tableau).T
        rows_idx = list(range(len(columns[0]) - 1))
        col_idx = list(range(len(columns) - 1))
        count = 0
        for i, col in enumerate(columns[:-1]):
            if self.is_basic(col):
                count = count + 1
                rows_idx.remove(np.argmax(col))
                col_idx.remove(np.argmax(col_idx))
        for i in range(len(columns[0]) - 1 - count):
            el_iter = itertools.product(rows_idx, col_idx)
            idx = next(el_iter)
            while self.tableau[idx[0]][idx[1]] == 0:
                idx = next(el_iter)
            self.next_step(idx[0], idx[1])
            rows_idx.remove(idx[0])
            col_idx.remove(idx[1])

    def to_tableau(self):
        """
        Creates a tableau looking like
        AA...AAB
        ........
        AA...AAB
        CC...CC0
        """
        xb = np.column_stack((self.a, self.b.T))
        z = np.column_stack(([self.c], [[self.ans]]))
        self.tableau = np.vstack((xb, z))

    @classmethod
    def read_from_file(cls, path: str):
        """Reads data written in file using specific format, return Simplex class"""
        with open(path, "r") as f:
            is_max = False
            if f.readline().strip() == 'max':
                is_max = True

            f.readline()
            c = [float(num) for num in f.readline().strip().split(',')]
            f.readline()

            a_matrix = []
            for line in f:
                if not line.strip():
                    break
                a_matrix.append([float(num) for num in line.strip().split(',')])

            b_matrix = [float(num) for num in f.readline().strip().split(',')]
            return cls(np.array(a_matrix), np.array(b_matrix), np.array(c), is_max)

    def can_be_improved(self) -> bool:
        """Returns true if ans could be improved <=> any c[j] > 0"""
        return any(x > 0 for x in self.c) if self.is_max else any(x < 0 for x in self.c)

    def find_solving_column(self) -> int:
        """Returns index of column that could be improved <=> j, c[j] >= c[i], i = 0..len(c)"""
        return np.argmax(self.c) if self.is_max else np.argmin(self.c)

    def find_solving_row(self, column_index: int) -> int:
        """Returns index of row with minimal restriction"""
        restrictions = []
        for row_index in range(self.a.shape[0]):
            el = self.a[row_index][column_index]
            restrictions.append(math.inf if el <= 0 else self.b[row_index] / el)

        row_index = restrictions.index(min(restrictions))

        if restrictions[row_index] == math.inf:
            raise Exception('No answer could be found. Range of valid values is infinite')
        return row_index

    def next_step(self, solving_row_index: int, solving_column_index: int):
        """Make iteration: find restrictions, edit tableau"""
        self.b[solving_row_index] /= self.a[solving_row_index][solving_column_index]
        self.a[solving_row_index] /= self.a[solving_row_index][solving_column_index]

        for row_index in range(self.a.shape[0]):
            if row_index == solving_row_index:
                continue

            self.b[row_index] -= self.b[solving_row_index] * self.a[row_index][solving_column_index]
            self.a[row_index] -= self.a[solving_row_index] * self.a[row_index][solving_column_index]

        self.ans -= self.b[solving_row_index] * self.c[solving_column_index]
        self.c -= self.a[solving_row_index] * self.c[solving_column_index]

        self.to_tableau()

    def solve(self) -> float:
        """Solves linear equasion system using simplex method"""

        while self.can_be_improved():
            solving_column_index = self.find_solving_column()
            solving_row_index = self.find_solving_row(solving_column_index)
            self.next_step(solving_row_index, solving_column_index)

        return -self.ans

    @staticmethod
    def is_basic(column: np.array) -> bool:
        return sum(column) == 1 and column.tolist().count(0) == len(column) - 1

    def get_solution(self):
        columns = self.tableau.T
        solutions = []
        for column in columns[:-1]:
            solution = 0
            if self.is_basic(column):
                one_index = column.tolist().index(1)
                solution = columns[-1][one_index]
            solutions.append(solution)

        return solutions


if __name__ == '__main__':
    for task_num in range(1, 9):
        simplex = Simplex.read_from_file(f'./input-files/task{task_num}.txt')
        print(f"task_{task_num}")
        print(simplex.solve())
        print(simplex.get_solution())
        print("_" * 100)
