# String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
# of another. Given two strings, si and s2, write code to check if s 2 is a rotation of si using only one
# call to isSubst ring (e.g., "water bottle" is a rotation of "erbottlewat").
# Hints: #34, #88, #104

def isSubstring(s1: str, s2: str):
    return s2.find(s1) != -1


def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        ss2 = s2 + s2
        return isSubstring(s1, ss2)


s1 = 'waterbottle'
s2 = 'erbottlewat'

print(isRotation(s1, s2))