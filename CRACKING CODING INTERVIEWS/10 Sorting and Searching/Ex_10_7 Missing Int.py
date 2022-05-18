# Missing Int: Given an input file with four billion non-negative integers, provide an algorithm to
# generate an integer that is not contained in the file. Assume you have 1 GB of memory available for
# this task.

# We will use numbers from 0 to 100

def missingIntUntil100(arr):
    numList = [0 for _ in range(100)]
    for k in arr:
        numList[k] = 1

    index = 0
    N = len(arr)
    while index < N:
        if numList[index] == 0:
            return index
        index += 1

    return -1


# arr = [3,55,23,1,2,4,56, 0]
arr = [0, 1, 2, 3, 5]
print(missingIntUntil100(arr))
