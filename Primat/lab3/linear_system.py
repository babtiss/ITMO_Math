from decompose_to_LU import *
from input import *


def step_1(L, B):
    n = L.shape[0]
    y = np.zeros_like(B, dtype=np.double)
    y[0] = B[0] / L[0, 0]
    for i in range(1, n):
        y[i] = (B[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    return y


def step_2(U, Y):
    n = U.shape[0]
    x = np.zeros_like(Y, dtype=np.double)
    x[-1] = Y[-1] / U[-1, -1]
    for i in range(n - 2, -1, -1):
        if U[i, i] == 0:
            x[i] = (Y[i] - np.dot(U[i, i:], x[i:])) / 10 ** -9
        else:
            x[i] = (Y[i] - np.dot(U[i, i:], x[i:])) / U[i, i]
    return x


def solve_(A, B):
    lu = decompose_to_LU(A)
    P, L, U = get_P(A), get_L(lu), get_U(lu)
    Y = step_1(L, P @ B)
    return step_2(U, Y)


def main():
    print(solve_(A, B))


if __name__ == "__main__":
    main()
