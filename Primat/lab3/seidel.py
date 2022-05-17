from input import *


def seidel(A, b, eps):
    n = len(A)
    x = np.zeros(n)

    while True:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))

            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        if np.allclose(x, x_new, rtol=eps):
            break

        x = x_new
    return x


def main():
    print(seidel(A, B, eps=10 ** -10))


if __name__ == "__main__":
    main()
