
#Description
"""
There are n guests attending a dinner party, numbered from 1 to n.
The ith guest has a height of arr[i-1] inches.
The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table.
As the host, you will choose how to arrange the guests,
one per seat. Note that there are n! possible permutations of seat assignments.
Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the
absolute difference between their two heights. Note that, because the table is circular, seats 1 and n are
considered to be adjacent to one another, and that there are therefore n pairs of adjacent guests.
The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent guests.
Determine the minimum possible overall awkwardness of any seating arrangement.
"""

import math
from itertools import permutations


# Add any extra import statements you may need here


# Add any helper functions you may need here
def awk(arr):
    awk = 0
    for i in range(len(arr)):
        awk = max(awk, abs(arr[i] - arr[i-1]))
    return awk


def minOverallAwkwardness(arr):
    # Write your code here
    minAwk = 1000
    perm = permutations(arr)
    for p in perm:
        minAwk = min(minAwk, awk(p))

    return minAwk


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
    arr_1 = [5, 10, 6, 8]
    expected_1 = 4
    output_1 = minOverallAwkwardness(arr_1)
    check(expected_1, output_1)

    arr_2 = [1, 2, 5, 3, 7]
    expected_2 = 4
    output_2 = minOverallAwkwardness(arr_2)
    check(expected_2, output_2)

    # Add your own test cases here
