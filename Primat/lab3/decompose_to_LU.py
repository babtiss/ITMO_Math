import numpy as np
from input import *

def decompose_to_LU(a):
    lu_matrix = np.matrix(np.zeros([a.shape[0], a.shape[1]]))
    n = a.shape[0]

    for k in range(n):
        for j in range(k, n):
            lu_matrix[k, j] = a[k, j] - lu_matrix[k, :k] * lu_matrix[:k, j]
        for i in range(k + 1, n):
            if lu_matrix[k, k] == 0:
                lu_matrix[i, k] = (a[i, k] - lu_matrix[i, : k] * lu_matrix[: k, k]) / 10 ** -9
            else:
                lu_matrix[i, k] = (a[i, k] - lu_matrix[i, : k] * lu_matrix[: k, k]) / lu_matrix[k, k]

    return lu_matrix


def get_L(m):
    L = m.copy()
    for i in range(L.shape[0]):
        L[i, i] = 1
        L[i, i + 1:] = 0
    return np.matrix(L)


def get_U(m):
    U = m.copy()
    for i in range(1, U.shape[0]):
        U[i, :i] = 0
    return U


def get_P(M):
    m = M.shape[0]

    new_matrix = [[float(i == j) for i in range(m)] for j in range(m)]

    for j in range(m):
        row = max(range(j, m), key=lambda x: abs(M[x][j]))
        if j != row:
            new_matrix[j], new_matrix[row] = new_matrix[row], new_matrix[j]

    matrix = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            matrix[i][j] = new_matrix[j][i]

    return matrix


def main():
    # init
    # A = np.array([[1, 2, 3],
    #               [2, 3, 4],
    #               [3, 4, 5]])

    # output
    lu = decompose_to_LU(A)
    print('U')
    print(get_U(lu))
    print('L')
    print(get_L(lu))
    print('P')
    print(np.matrix(get_P(A)))


if __name__ == "__main__":
    main()
