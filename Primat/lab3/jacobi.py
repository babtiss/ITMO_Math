import time

from input import *


def solve(A, B):
    x = np.zeros_like(B)
    while True:

        x_new = np.zeros_like(x)

        for i in range(A.shape[0]):
            s = np.array([A[i][j] if j != i else 0 for j in range(len(A))]).dot(x[:])
            if A[i, i] < 10 ** -9:
                x_new[i] = (B[i] - s) / 10 ** -9
            else:
                x_new[i] = (B[i] - s) / A[i, i]
            if x_new[i] == x_new[i - 1]:
                break
        if np.allclose(x, x_new, rtol=1e-6):
            break

        x = x_new
    print(x)


def main():
    solve(A, B)



if __name__ == "__main__":
    main()
