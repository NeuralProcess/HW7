#Solve the equation AX=b by Doolittle's decomposition method

import numpy as np

a_matrix = np.matrix([[2.34, -4.10, 1.78],\
                      [-1.98, 3.47, -2.22],\
                      [2.36, -15.17, 6.18]])
print(a_matrix)

b_matrix = np.matrix([[0.02], [-0.73], [-6.63]])
print(b_matrix)


def lu_decompose(mat):
    rows, columns = mat.shape
    s = min(rows, columns)  # to determine s: (row by s) @ (s by colunns)
    print(s)

    for k in range(s):
        x = 1 / mat[k, k]
        print(k, '번째 x는', x, '입니다.')
        for i in range(k + 1, rows):
            mat[i, k] = mat[i, k] * x
            print(i, '번째 mat는', mat[i, k], '입니다.')
        for i in range(k + 1, rows):
            for j in range(k + 1, columns):
                mat[i, j] = mat[i, j] - mat[i, k] * mat[k, j]
                print(j, '번째 mat는 ', mat[i, j], '입니다.')

    L = np.tril(mat, k=-1) + np.identity(rows)
    U = np.triu(mat, k=0)
    return L, U


mat = np.array([[1, 2, 3],
                [2, 6, 4],
                [8, 9, 1]])

L, U = lu_decompose(mat)

print(L)
print(U)

