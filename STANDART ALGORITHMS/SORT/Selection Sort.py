# Selection sort is the child's algorithm: simple, but inefficient. Find the smallest element using a linear scan
# and move it to the front (swapping it with the front element). Then, find the second smallest and move it,
# again doing a linear scan. Continue doing this until all the elements are in place.

from random import randrange


def selectionSort(arr):
    N = len(arr)
    # go to all positions
    for i in range(N-1):
        indexMin = i
        mini = arr[i]
        # find the minimum in [i,N] and put it in i
        for k in range(i, N-1):
            if arr[k + 1] < mini:
                indexMin = k + 1
                mini = arr[k + 1]
        temp = arr[indexMin]
        arr[indexMin] = arr[i]
        arr[i] = temp


arr = [randrange(1, 20) for _ in range(10)]
print(arr)
selectionSort(arr)
print(arr)
