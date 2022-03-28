import matplotlib.pyplot as plt

from input import *

from task1 import dichotomy_method

x = [10 ** (-i) for i in range(2, 10)]
y = [dichotomy_method(A, B, epsilon)[3] for epsilon in x]
plt.figure(figsize=(9, 9))
plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.title("f_invocations(epsilon)")
plt.xlabel("epsilon", fontsize=14)
plt.ylabel("f_invocations", fontsize=14)
plt.grid(True)
plt.show()
