import numpy as np

def mat_access1(mat):

    for i in range(mat.shape[0]):
        for j in range (mat.shape[1]):
            print(mat[i][j])


mat1 = np.arange(10).reshape(2,5)
mat2 = np.arange(10).reshape(2,5)

mat_access1(mat1)

