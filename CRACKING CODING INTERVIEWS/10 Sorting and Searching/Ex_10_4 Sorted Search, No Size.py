# You are given an array-like data structure Li sty which lacks a size
# method. It does, however, have an elementAt (i) method that returns the element at index i in
# 0(1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
# structure only supports positive integers.) Given a Listy which contains sorted, positive integers,
# find the index at which an element x occurs. If x occurs multiple times, you may return any index.

class integerNoSizeList:
    def __init__(self, arr: list):
        self.arr = arr

    def valueAt(self, i):
        if i < len(self.arr):
            return self.arr[i]
        return -1


def sortedSearch(arr, x, left, right):
    while not left == right:
        mid = (left + right) // 2
        if arr.valueAt(mid) == -1:
            right = mid - 1
        else:
            if arr.valueAt(mid) == x:
                return mid
            if arr.valueAt(mid) > x:
                right = mid - 1
            else:
                left = mid + 1

    if arr.valueAt(left) == x:
        return left
    return -1


def sortedSearchNoSize(myList: integerNoSizeList, x):
    index = 0
    jump = 1
    while 0 <= myList.valueAt(index) < x:
        index += jump
        jump *= 2
    if myList.valueAt(index - int(jump / 2)) == x:
        return index

    return sortedSearch(myList, x, index - int(jump / 2), index)


lst = list(range(21))
arr = integerNoSizeList(lst)
print(lst)
print(sortedSearchNoSize(arr, 20))
