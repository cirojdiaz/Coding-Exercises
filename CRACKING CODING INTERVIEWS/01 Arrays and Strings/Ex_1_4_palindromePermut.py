# a word is a permutation of a palindrome word if it has a
# even number of letter with even frequencies
# an odd number of letters with even frequencies except for one.
# (Spaces don't count)

def is_perm_of_palindrome(myStr: str):
    # Removing spaces
    myStr = ''.join(e for e in myStr if e != ' ')
    # Get the frequencies
    freq = dict()
    for c in myStr:
        if c in freq.keys():
            freq[c] += 1
        else:
            freq[c] = 1
    # cases odd and even
    odd_num = 0
    if len(myStr) % 2 == 0:
        for v in freq.values():
            if v % 2 != 0:
                return False
    else:
        for v in freq.values():
            if v % 2 != 0:
                if odd_num > 1:
                    return False
                else:
                    odd_num += 1
    return True

s = 'aa hhb b ccxxxgyy'
print('String "{}" is {}a permutation of a Palindrome'.format(s, 'Not ' * (not is_perm_of_palindrome(s))))