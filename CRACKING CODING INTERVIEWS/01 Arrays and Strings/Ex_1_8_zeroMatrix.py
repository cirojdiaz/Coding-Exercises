# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.
from random import randint


def randMat(n, m):
    return [[randint(0, 9) for mm in range(m)] for nn in range(n)]


n, m = 6, 7
mat = randMat(n, m)
for nn in range(n):
    print(mat[nn])


def find_zeros(mat):
    n = len(mat)
    m = len(mat[0])
    zeros = [(nn, mm) for nn in range(n) for mm in range(m) if mat[nn][mm] == 0]
    return zeros


zeros = find_zeros(mat)


def zero_row_col(mat, zeros):
    n = len(mat)
    m = len(mat[0])
    zrc = [[mat[nn][mm] for mm in range(m)] for nn in range(n)]
    for nn, mm in zeros:
        for _ in range(m):
            zrc[nn][_] = 0
        for _ in range(n):
            zrc[_][mm] = 0
    return zrc


zrc = zero_row_col(mat, zeros)
print('With zeros')
for row in zrc:
    print(row)
