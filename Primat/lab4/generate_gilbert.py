import numpy
import scipy


def generate(n):
    a = numpy.matrix([[1 / (i + j - 1) for i in range(1, n + 1)] for j in range(1, n + 1)])
    matrix = scipy.sparse.__dict__["lil_matrix"]((n, n))

    for i in range(n):
        for j in range(i, n):
            matrix[i, j] = a[i, j]
            matrix[j, i] = a[i, j]
    return matrix


if __name__ == "__main__":
    generate(5)
