# META Strings are a permutation of each others

def is_perm(s1, s2):
    l1 = sorted([ord(c) for c in s1])
    l2 = sorted([ord(c) for c in s2])
    for a, b in zip(l1, l2):
        if a != b:
            return False
    return True


s1 = 'Canadaa'
s2 = 'nadaCda'

print('String "{}" is {}a permutation of string "{}"'.format(s1, 'NOT ' * (not is_perm(s1, s2)), s2))
