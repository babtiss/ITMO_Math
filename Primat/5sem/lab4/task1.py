import numpy as np
import pandas as pd


def random_sample(n):
    params = np.random.uniform(-1, 1, (n, 2))
    target = np.array([x ** 2 + y ** 2 > 0.25 for x, y in params])
    return pd.DataFrame(np.hstack((params, target.reshape(-1, 1))), columns=["x", "y", "target"])


if __name__ == "__main__":
    print("TASK1___example")
    print(random_sample(2))
