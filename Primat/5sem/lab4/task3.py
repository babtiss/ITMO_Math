from task2 import *
from task1 import *
import matplotlib.pyplot as plt

from sklearn.svm import NuSVC
from sklearn.model_selection import train_test_split
from sklearn.inspection import DecisionBoundaryDisplay


def solve_a():
    SIZE = 3_500
    kernels = ["linear", "poly", "rbf", "sigmoid"]

    data_kernel = {}
    for kernel in kernels:
        model = NuSVC(nu=0.1, kernel=kernel, gamma=10)
        sample = random_sample(SIZE)
        x_train, x_test, y_train, y_test = train_test_split(sample[["x", "y"]], sample.target, test_size=0.3)

        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        data_kernel[kernel] = {}
        data_kernel[kernel]["accuracy"] = accuracy_score(y_test, y_pred),
        data_kernel[kernel]["recall"] = recall_score(y_test, y_pred),
        data_kernel[kernel]["precision"] = precision_score(y_test, y_pred),
        data_kernel[kernel]["f1"] = precision_score(y_test, f_score(y_test, y_pred)),
        DecisionBoundaryDisplay.from_estimator(
            model, x_test, response_method="predict", alpha=0.5, xlabel="x", ylabel="y")
        plt.scatter(x_test.x, x_test.y, c=y_test)
        plt.xlim([-1, 1])
        plt.ylim([-1, 1])
        plt.title(f"Kernel: {kernel}")
        plt.show()

    data_kernel_df = pd.DataFrame(data_kernel).T
    print(data_kernel_df)
    data_kernel_df.plot.bar(rot=0, figsize=(20, 10), ylim=(0, 1.01))
    plt.show()


def solve_b():
    samp_sizes = [100, 1000, 3_000, 5_000, 10_000, 50_000]

    data_samp = {}
    for sample_size in samp_sizes:
        model = NuSVC(nu=0.1, kernel="rbf", gamma=10)
        sample = random_sample(sample_size)
        x_train, x_test, y_train, y_test = train_test_split(sample[["x", "y"]], sample.target, test_size=0.3)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        data_samp[sample_size] = {}
        data_samp[sample_size]["accuracy"] = accuracy_score(y_test, y_pred),
        data_samp[sample_size]["recall"] = recall_score(y_test, y_pred),
        data_samp[sample_size]["precision"] = precision_score(y_test, y_pred),
        data_samp[sample_size]["f1"] = precision_score(y_test, f_score(y_test, y_pred)),

    data_kernel_df = pd.DataFrame(data_samp).T
    print(data_kernel_df)
    data_kernel_df.plot.bar(rot=0, figsize=(20, 10), ylim=(0.89, 1.01))
    plt.show()


def solve_c():
    lower_bounds_sv = [0.01, 0.06, 0.11, 0.16, 0.21, 0.26]

    SIZE = 3_500
    data_nu = {}
    for lower_bound in lower_bounds_sv:
        lower_bound = lower_bound
        model = NuSVC(nu=lower_bound, kernel="rbf", gamma=10)
        sample = random_sample(SIZE)
        x_train, x_test, y_train, y_test = train_test_split(sample[["x", "y"]], sample.target, test_size=0.3)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        data_nu[lower_bound] = {}
        data_nu[lower_bound]["accuracy"] = accuracy_score(y_test, y_pred),
        data_nu[lower_bound]["recall"] = recall_score(y_test, y_pred),
        data_nu[lower_bound]["precision"] = precision_score(y_test, y_pred),
        data_nu[lower_bound]["f1"] = precision_score(y_test, f_score(y_test, y_pred)),
        DecisionBoundaryDisplay.from_estimator(model, x_test, response_method="predict", alpha=0.5, xlabel="x",
                                               ylabel="y")
        plt.scatter(x_test.x, x_test.y, c=y_pred)
        plt.xlim([-1, 1])
        plt.ylim([-1, 1])
        plt.title(f"Nu: {lower_bound}")
        plt.show()
    data_nu_df = pd.DataFrame(data_nu).T
    print(data_nu_df)
    data_nu_df.plot.bar(rot=0, figsize=(20, 10), ylim=(0.89, 1.01))
    plt.show()


if __name__ == "__main__":
    # solve_a()
    # solve_b()
    solve_c()
