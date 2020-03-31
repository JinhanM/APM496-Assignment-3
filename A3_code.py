import numpy as np
import scipy.linalg as lina
import matplotlib.pyplot as plt

# Q1.1
A = np.array([[1/2, 1/4, 1/8, 1/8], [0, 5/8, 1/4, 1/8], [0, 0, 3/4, 1/4], [0, 0, 0, 1]])
print("A^2 is : \n", np.linalg.matrix_power(A, 2), "\n")

print("A^(1/2) is : \n", lina.sqrtm(A), "\n")

x = np.arange(1, 100)
y = (1/2) ** x

plt.plot(x, y)
plt.show()


y = np.zeros(shape=(99,))
for i in range(len(x)):
    y[i] = np.linalg.matrix_power(A, i)[0][-1]


plt.plot(x, y)
plt.show()
