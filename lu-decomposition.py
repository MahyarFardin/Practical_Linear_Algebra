import numpy as np
from scipy.linalg import lu
import time


def lu_decomposition(matrix):
    n = len(matrix)
    L = np.ones((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += (L[i, k] * U[k, j])
            U[i, j] = matrix[i, j] - sum

        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += (L[j, k] * U[k, i])
            L[j, i] = (matrix[j, i] - sum) / U[i, i]

    return L, U


size = 100
execution_time_custom = 0
execution_time_scpy = 0
for i in range(1000):
    matrix = np.random.rand(size, size)
    start_time = time.time()
    L, U = lu_decomposition(matrix)
    end_time = time.time()
    execution_time_custom += end_time - start_time

for i in range(1000):
    matrix = np.random.rand(size, size)
    start_time = time.time()
    P, L, U = lu(matrix)
    end_time = time.time()
    execution_time_scpy += end_time - start_time


print("Execution time for custom LU decomposition implemented from scratch:", execution_time_custom * 1000, "ms")
# 281742.60807037354 ms
print("Execution time for scipy's built-in LU decomposition:", execution_time_np * 1000, "ms")
# 1318.2616233825684 ms
