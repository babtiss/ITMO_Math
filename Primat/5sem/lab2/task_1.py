import numpy


def is_pure(matrix):
    max_min = None
    min_max = None
    x = -1
    y = -1

    for i in range(len(matrix)):
        cur_max = min(matrix[i])
        if max_min is None or cur_max > max_min:
            max_min = cur_max
            y = i

    for i in range(len(matrix[0])):
        cur_min = max(matrix[:, i])
        if min_max is None or cur_min < min_max:
            min_max = cur_min
            x = i

    if min_max == max_min:
        return True, y, x, max_min
    else:
        return False, -1, -1, -1


def main():
    matrix = numpy.array([
        [90.0, 76.5, 91.5, 91.5],
        [103.5, 90.0, 91.5, 103.5],
        [88.5, 88.5, 90.0, 103.5],
        [88.5, 76.5, 76.5, 90.0]
    ])
    print(is_pure(matrix))


if __name__ == "__main__":
    main()
