"""
You are given two strings s and t.
You can select any substring of string s and rearrange the characters of the selected substring.
Determine the minimum length of the substring of s such that string t is a substring of the selected substring.
"""

from collections import deque, defaultdict


def min_length_substring(s, t):
    # Write your code here
    Sfreq = dict()
    Tfreq = dict()

    for _ in t:
        if _ not in Tfreq:
            Tfreq[_] = 0
            Sfreq[_] = 0
        Tfreq[_] += 1

    IsFull = False
    Index = deque([])

    for i, es in enumerate(s):

        if es in Tfreq:
            if not IsFull:
                Sfreq[es] += 1
                allIn = [Tfreq[key] > Sfreq[key] for key in Sfreq]
                if not any(allIn):  # Check if I have everybody
                    IsFull = True
                Index.append(i)
            elif IsFull:
                if es == s[Index[0]] and Index[-1] - Index[0] >= i - Index[2]:
                    Sfreq[s[Index.popleft()]] -= 1
                    Index.append(i)
                    Sfreq[s[Index[-1]]] += 1
                    while Sfreq[s[Index[0]]] > Tfreq[s[Index[0]]]:  # Reduce the first part of the substr
                        Sfreq[s[Index.popleft()]] -= 1

    if not IsFull:
        return -1
    subStr = s[Index[0]:Index[-1]+1]
    print(subStr)
    return len(subStr)


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
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

    s3 = "xxxbxxaaxxcxcbaxcxxbbxa"
    t3 = "abcc"
    expected_3 = 5
    output_3 = min_length_substring(s3, t3)
    check(expected_3, output_3)

    # Add your own test cases here
