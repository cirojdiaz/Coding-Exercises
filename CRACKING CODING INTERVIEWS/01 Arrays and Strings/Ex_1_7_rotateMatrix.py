# Rotate 90 degrees

from random import randint


# create the matrix 5X6

def randMat(n, m):
    return [[randint(0, 16) for mm in range(m)] for nn in range(n)]

n, m = 6, 7
mat = randMat(6, 7)
for nn in range(n):
    print(mat[nn])


def transpose(mat):
    n = len(mat)
    m = len(mat[0])
    return [[mat[nn][mm] for nn in range(n)] for mm in range(m)]


mat = transpose(mat)

mat = [mat[k] for k in range(m-1, -1, -1)]
for mm in range(m):
    print(mat[mm])


