"""
We have N different apps with different user growth rates.
At a given time t, measured in days, the number of users using an app is g^t (for simplicity we'll allow fractional users),
where g is the growth rate for that app.
These apps will all be launched at the same time and no user ever uses more than one of the apps.
We want to know how many total users there are when you add together the number of users from each app.
After how many full days will we have 1 billion total users across the N apps?
"""

import math


# Add any extra import statements you may need here


# Add any helper functions you may need here


def getBillionUsersDay(growthRates):
    # Write your code here
    t, Sum = 1, 0
    right = 1
    S = 0
    # Find an uper bound
    while S <= 10 ** 9:
        left = right
        right *= 2
        S = math.floor(sum([g ** right for g in growthRates]))

    while right-left > 1:
        midle = (left + right) / 2
        S = math.floor(sum([g ** midle for g in growthRates]))
        if S == 10 ** 9:
            return math.floor(midle)
        elif S < 10 ** 9:
            left = midle
        else:
            right = midle

    return math.floor(right)



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
    test_1 = [1.1, 1.2, 1.3]
    expected_1 = 79
    output_1 = getBillionUsersDay(test_1)
    check(expected_1, output_1)

    test_2 = [1.01, 1.02]
    expected_2 = 1047
    output_2 = getBillionUsersDay(test_2)
    check(expected_2, output_2)

    # Add your own test cases here
