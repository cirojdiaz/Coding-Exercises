import math


# Add any extra import statements you may need here


# Add any helper functions you may need here
def bubleFit(arr, e):
    arr.append(e)
    k = len(arr)-1
    while k > 0 and arr[k-1] > arr[k]:
        tmp = arr[k-1]
        arr[k-1] = arr[k]
        arr[k] = tmp
        k -= 1
    return arr


def findMedian(arr):
    # Write your code here
    arrOrd = [arr[0]]
    output = [arr[0]]
    pos = 0
    for e in arr[1:]:
        pos += 1
        arrOrd = bubleFit(arrOrd, e)
        if pos % 2 == 1:
            median = (arrOrd[(pos - 1) // 2] + arrOrd[(pos - 1) // 2 + 1]) / 2
        else:
            median = arrOrd[math.floor(pos / 2)]
        output.append(median)
    return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [5, 15, 1, 3]
    expected_1 = [5, 10, 5, 4]
    output_1 = findMedian(arr_1)
    check(expected_1, output_1)

    arr_2 = [2, 4, 7, 1, 5, 3]
    expected_2 = [2, 3, 4, 3, 4, 3]
    output_2 = findMedian(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
