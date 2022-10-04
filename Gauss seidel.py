import math
import numpy as np


def norm(x1, x0):
    x = [0 for i in range(len(x1))]
    for i in range(len(x1)):
        x[i] = x1[i] - x0[i]
    s = [i ** 2 for i in x]
    res = math.sqrt(sum(s))
    return res


def norm1(A):
    n = len(A)
    s = 0
    s1 = 0
    for j in range(n):
        for i in range(n):
            s1 += abs(A[i][j])
        if j == 0:
            s = s1
        else:
            s = max(s, s1)
        s1 = 0
    return s


def calSum(A, x0, x1, i):
    s = 0
    for t in range(i):
        s += A[t] * x0[t]
    for t in range(i + 1, len(A)):
        s += A[t] * x1[t]
    return s


def convergence(A):
    n = len(A)
    L = [[0 for x in range(n)] for y in range(n)]
    D = [[0 for x in range(n)] for y in range(n)]
    U = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            if i < j:
                L[i][j] = A[i][j]
            elif i == j:
                D[i][j] = A[i][j]
            else:
                U[i][j] = A[i][j]
    L = np.array(L)
    D = np.array(D)
    U = np.array(U)
    M = np.dot(np.linalg.inv(np.add(D, L)), U)
    if norm1(M) < 1:
        return True
    return False


n = int(input("Enter the dimension of the matrix A (in the equation Ax = b): "))
A = [[0 for x in range(n)] for y in range(n)]
for i in range(n):
    temp = input("Enter the " + str(i + 1) + "th row of matrix A(example: 1 , 2 , 3): ").split(" , ")
    A[i] = [float(x) for x in temp]
temp = input("Enter matrix B(example: 1 , 2 , 3): ").split(" , ")
B = [float(x) for x in temp]
epsilon = float(input("Enter epsilon for stopping criteria: "))

if convergence(A):
    limit = epsilon + 1
    x0 = [0 for i in range(n)]
    x1 = [0 for i in range(n)]
    while limit >= epsilon:
        x1 = list.copy(x0)
        for i in range(n):
            x0[i] = B[i] / A[i][i] - (calSum(A[i], x0, x1, i)) / A[i][i]

        limit = norm(x0, x1)
    print(x0)
else:
    print("This method diverges with the given matrices!")
