import math

# Add any extra import statements you may need here


# Add any helper functions you may need here

# Naive way O(N**2)
"""
def numberOfWays(arr, k):
  # Write your code here
  cnt = 0
  for i in range(len(arr)-1):
    for e in arr[i+1:]:
      if arr[i]+e == k:
        cnt += 1
  return cnt
"""

# If k is not that large
"""
def numberOfWays(arr, k):
    freq = [0 for _ in range(0, k + 1)]
    cnt = 0
    for e in arr:
        if e <= k:
            freq[e] += 1

    for i in range(k // 2):
        cnt += freq[i] * freq[k - i]

    if k % 2 == 0:
        cnt += freq[k//2]*(freq[k//2]-1)/2

    return cnt
"""


#  If k can be very large we Sort
def numberOfWays(arr, k):
    ways = 0
    arr = list(sorted(arr))
    left = 0
    right = len(arr) - 1
    while arr[left] < arr[right]:
        if arr[left] + arr[right] == k:
            l_old, r_old = left, right
            l_freq, r_freq = 0, 0
            while arr[left] == arr[l_old]:
                l_old = left
                left += 1
                l_freq += 1
            while arr[right] == arr[r_old]:
                r_old = right
                right -= 1
                r_freq += 1
            ways += l_freq * r_freq

        elif arr[left] + arr[right] > k:
            r_old = right
            while arr[right] == arr[r_old]:
                r_old = right
                right -= 1

        else:
            l_old = left
            while arr[left] == arr[l_old]:
                l_old = left
                left += 1

    if arr[left] == arr[right]:
        freq = 0
        while left <= right:
            l_old = left
            left += 1
            freq += 1
        ways += freq * (freq - 1) / 2

    return ways


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
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = numberOfWays(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3]
    expected_2 = 4
    output_2 = numberOfWays(arr_2, k_2)
    check(expected_2, output_2)

    # Add your own test cases here
