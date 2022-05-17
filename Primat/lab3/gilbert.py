import numpy
from datetime import datetime
import seidel


def main():
    for n in range(100, 2000, 100):
        start = datetime.now()
        a = numpy.array([[1 / (i + j - 1) for i in range(1, n + 1)] for j in range(1, n + 1)])
        b = numpy.array([sum(a[i]) for i in range(n)])

        seidel.seidel(a, b, eps=0.01)
        end = datetime.now()
        print(n, end - start)


if __name__ == "__main__":
    main()
