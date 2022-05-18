# In bubble sort, we start at the beginning of the array and swap the first two elements if the first is greater
# than the second.Then, we go to the next pair, and so on, continuously making sweeps of the array until it is
# sorted. In doing so, the smaller items slowly "bubble" up to the beginning of the list.


# Iterative
def bubbleSort(arr):
    N = len(arr) - 1
    for i in range(N):
        for k in range(N):
            if arr[k] > arr[k + 1]:
                temp = arr[k + 1]
                arr[k + 1] = arr[k]
                arr[k] = temp
    return arr


arr = list(range(11, -1, -1))
print(arr)
print(bubbleSort(arr))
