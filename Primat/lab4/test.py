import scipy
import scipy.sparse as sps
import numpy as np
from matplotlib import pyplot as plt
from numpy import diag
from math import atan, cos, sin, pi
from generate_gilbert import generate

import random


def maxElem(A, n):
    aMax, k, l = 0.0, 0, 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(A[i, j]) >= aMax:
                aMax = abs(A[i, j])
                k = i
                l = j
    return k, l


def makeEmatrix(n):
    eMatrix = sps.csr_matrix(sps.rand(n, n, density=0.0))
    eMatrix.setdiag(1)
    return eMatrix


def rotate(A, n, k, l):
    U = makeEmatrix(n)
    if A[k, k] != A[l, l]:
        phi = 0.5 * atan((2 * A[k, l]) / (A[k, k] - A[l, l]))
    else:
        phi = pi / 4
    phi = phi
    U[k, k], U[l, l] = cos(phi), cos(phi)
    U[k, l], U[l, k] = -sin(phi), sin(phi)
    U_transp = U.transpose()

    A1 = (U_transp.dot(A)).dot(U)
    return A1, U


def norm(A, n):
    sum = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum += A[i, j] ** 2
    return sum ** 0.5


def jacobi(A, n, eps):
    U = makeEmatrix(n)
    iteration = 0
    while norm(A, n) > eps:
        k, l = maxElem(A, n)
        A1, Utemp = rotate(A, n, k, l)
        A = A1
        U *= Utemp
        iteration += 1
    return diag(A.toarray()), U, iteration


def generateSimMatrix(n):
    example = np.matrix([[random.randint(0, 10) for _ in range(n)] for _ in range(n)])

    sum_example = n ** 2 * 10

    for i in range(n):
        example[i, i] = sum_example + random.randint(1, 10)

    matrix = scipy.sparse.__dict__["lil_matrix"]((n, n))

    for i in range(n):
        for j in range(i, n):
            matrix[i, j] = example[i, j]
            matrix[j, i] = example[i, j]
    return matrix


def mult(matr, vect, n):  # умножение матрицы на вектор справа (лень копаться, как это пишется в Numpy)
    r = []
    for i in range(n):
        s = 0.0
        for j in range(n):
            s += matr[i, j] * vect[j]
        r += [s]
    return r


def check_our_solution(A, matrix_solve, lambda_A, n):
    ve = []
    for i in range(n):
        ve.append(matrix_solve[i][0])

    print("vve", ve)
    rr = mult(A, ve, n)  # умножаем собственный вектор на исходную матрицу

    for i in range(n):
        print('actual = ', rr[i] / ve[i], '; expected =',
              lambda_A)  # делим соотв. координаты произведения и исходного вектора друг на друга


y = []
x = []
for n in range(5, 29, 1):
    A = generateSimMatrix(n)
    # A = generate(n)
    # print(A.todense())
    eigenvalues, U, it = jacobi(A, n, 1e-3)

    # print("---------------[Eigenvalues Jakobi lamdas]---------------\n")
    # print(f"{eigenvalues}\n")
    # print("---------------[Eigenvectors Jakobi]---------------\n")
    # print(f"{U.toarray()}\n")
    # check_our_solution(A, U.toarray(), eigenvalues[0], n)
    x.append(n)
    y.append(it)

y1 = []
for n in range(5, 29, 1):
    A = generateSimMatrix(n)
    # A = generate(n)
    # print(A.todense())
    eigenvalues, U, it = jacobi(A, n, 1e-6)

    # print("---------------[Eigenvalues Jakobi lamdas]---------------\n")
    # print(f"{eigenvalues}\n")
    # print("---------------[Eigenvectors Jakobi]---------------\n")
    # print(f"{U.toarray()}\n")
    # check_our_solution(A, U.toarray(), eigenvalues[0], n)
    y1.append(it)
y2 = []
for n in range(5, 29, 1):
    A = generateSimMatrix(n)
    # A = generate(n)
    # print(A.todense())
    eigenvalues, U, it = jacobi(A, n, 1e-9)

    # print("---------------[Eigenvalues Jakobi lamdas]---------------\n")
    # print(f"{eigenvalues}\n")
    # print("---------------[Eigenvectors Jakobi]---------------\n")
    # print(f"{U.toarray()}\n")
    # check_our_solution(A, U.toarray(), eigenvalues[0], n)
    y2.append(it)

plt.figure(figsize=(9, 9))
plt.plot(x, y, "b")
plt.plot(x, y1, "r")
plt.plot(x, y2, "y")
plt.xlabel("n", fontsize=14)
plt.ylabel("iteration", fontsize=14)
plt.grid(True)
plt.show()
