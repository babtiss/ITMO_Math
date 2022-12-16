import numpy as np


def main():
    x = np.array([6 / 13, 3 / 13, 4 / 13])
    y = np.array([6 / 13, 4 / 13, 3 / 13])
    matrix = np.array([
        [1, -1, -1],
        [-1, -1, 3],
        [-1, 2, -1]
    ])

    print("Матожидание проигрыша первого игрока: ", -(x @ matrix @ y.T))


if __name__ == '__main__':
    main()