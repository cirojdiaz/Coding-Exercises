"""
Given two strings s and t of length N, find the maximum number of possible matching
pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that
is present at the ith and jth index of s, respectively.
The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
Note: This means you must swap two characters at different indices.
"""

def matching_pairs(s, t):
    if s == t:
        if len(set(s)) == len(s):  # If there are no repeated characters
            return len(s) - 2
        return len(s)  # identical characters will be switched to obtain the same array

    unmatched_pairs, unmatched_in_t, unmatched_in_s = set(), set(), set()
    found_perfect_swap, partial_swap = False, False
    count = 0

    for i in range(len(s)):
        if s[i] == t[i]:
          count += 1
        else:
            unmatched_pairs.add((s[i], t[i]))
            unmatched_in_t.add(t[i])
            unmatched_in_s.add(s[i])
            if (t[i], s[i]) in unmatched_pairs:
                found_perfect_swap = True
            elif s[i] in unmatched_in_t or t[i] in unmatched_in_s:
                partial_swap = True

    if found_perfect_swap:
        return count + 2
    elif partial_swap:
        return count + 1


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
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here
