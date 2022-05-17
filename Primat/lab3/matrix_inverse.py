from linear_system import *
from decompose_to_LU import *
from input import *


def solve_inverse_matrix(A):
    n = A.shape[0]
    lu = decompose_to_LU(A)
    b = np.array([[1 if i == j else 0 for i in range(n)] for j in range(n)])
    A_inverse = np.zeros((n, n))
    P, L, U = get_P(A), get_L(lu), get_U(lu)
    for i in range(n):
        y = step_1(L, np.dot(P, b[i, :]))
        A_inverse[i, :] = step_2(U, y)
    return A_inverse


def main():

    A = np.array([[10., -1., 2., 0.],
                  [-1., 11., -1., 3.],
                  [2., -1., 10., -1.],
                  [0.0, 3., -1., 8.]])

    # output
    print("matrix inverse")
    print(solve_inverse_matrix(A))
    # check
    print("Check")
    print(A.dot(solve_inverse_matrix(A)))


if __name__ == "__main__":
    main()
