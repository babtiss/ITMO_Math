import numpy as np
import matplotlib.pyplot as plt


def analytically_compute_probability_vec(transition_matrix):
    equations = transition_matrix.transpose()
    equations -= np.identity(equations.shape[0])

    last_equation = np.ones((1, equations.shape[1]))
    equations = np.append(equations, last_equation, axis=0)

    ordinate = np.zeros(equations.shape[0])
    ordinate[-1] = 1

    probability_vec = np.linalg.lstsq(equations, ordinate, rcond=None)[0]

    return probability_vec


def numerically_compute_probability_vec(
        p, P, eps=0.0001, steps=10 ** 3):
    step = 0
    stds = []

    while not np.linalg.norm(p @ P - p) < eps and step <= steps:
        step += 1

        stds.append(np.linalg.norm(p @ P - p))

        p = p @ P

    return p / p.sum(), stds


if __name__ == "__main__":
    P = np.array([
        [0.1, 0.3, 0, 0, 0.6, 0, 0, 0],
        [0.4, 0.1, 0, 0, 0.2, 0.1, 0.2, 0],
        [0, 0.1, 0.2, 0, 0, 0, 0.7, 0],
        [0, 0, 0, 0.1, 0, 0, 0.4, 0.5],
        [0.1, 0.2, 0, 0, 0.5, 0.2, 0, 0],
        [0, 0.1, 0, 0, 0.1, 0.2, 0.6, 0],
        [0, 0, 0.2, 0.2, 0, 0.3, 0.1, 0.2],
        [0, 0, 0, 0.2, 0, 0, 0.5, 0.3],
    ])
    p1 = np.array([1., 0, 0, 0, 0, 0, 0, 0])
    p2 = np.array([0, 1., 0, 0, 0, 0, 0, 0])

    # === Test ===
    num_prob1, stds1 = numerically_compute_probability_vec(p1, P)
    num_prob2, stds2 = numerically_compute_probability_vec(p2, P)
    an_prob = analytically_compute_probability_vec(P)

    with np.printoptions(precision=3):
        print("Numerical solution 1:", num_prob1)
        print("Numerical solution 1:", num_prob2)
        print("Analytical solution:", an_prob)

    plt.xlabel('step')
    plt.ylabel('std')
    plt.plot(range(0, len(stds1)), stds1)
    plt.plot(range(0, len(stds2)), stds2)
    plt.show()
