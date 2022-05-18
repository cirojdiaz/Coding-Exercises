import math


# Add any extra import statements you may need here


# Add any helper functions you may need here
def getMaxPos(arr):
    max = arr[0]
    pos = 0
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
            pos = i
    return max, pos


def dropPos(arr, pos):
    if pos == 0:
        return arr[1:]
    return arr[0:pos] + arr[pos + 1:]


def getTotalTime(arr):
    # Write your code here
    penalty = 0
    while len(arr) > 1:
        m1, p1 = getMaxPos(arr)
        arr = dropPos(arr, p1)
        m2, p2 = getMaxPos(arr)
        penalty += m1 + m2
        arr[p2] = m1 + m2

    return penalty


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    arr_1 = [4, 2, 1, 3]
    expected_1 = 26
    output_1 = getTotalTime(arr_1)
    check(expected_1, output_1)

    arr_2 = [2, 3, 9, 8, 4]
    expected_2 = 88
    output_2 = getTotalTime(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
