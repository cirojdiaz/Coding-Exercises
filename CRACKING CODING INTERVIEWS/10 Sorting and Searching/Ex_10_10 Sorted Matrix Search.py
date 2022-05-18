# Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
# ascending order, write a method to find an element.

def sortedMatrixSearch(mat, x):
    Left = 0
    Right = len(mat[0]) - 1
    Up = 0
    Down = len(mat) - 1
    searchRow = True
    while Left < Right or Up < Down:
        midVertical = (Down + Up) // 2
        midHorizontal = (Right + Left) // 2
        if mat[midVertical][midHorizontal] == x:
            return midVertical, midHorizontal
        if mat[midVertical][midHorizontal] > x:
            if searchRow:
                Right = midHorizontal - 1
            else:
                Down = midVertical - 1
        else:
            if searchRow:
                Left = midHorizontal + 1
            else:
                Up = midVertical + 1
        searchRow = searchRow == False

    if mat[Up][Left] == x:
        return Up, Left
    return -1


mat = [[1, 2, 3], [4, 6, 9], [5, 7, 20]]
for row in mat:
    print(row)

print(sortedMatrixSearch(mat, 2))
