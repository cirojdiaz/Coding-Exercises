# Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to
# each other.
# Hin ts: #177, #182, #263, #342

s1 = ['ab', 'cd', 'ba', 'dc', 'hj', 'ab', 'nuy', 'cba']


def grupAnagrams(strList: str):
    anagrams = dict()
    for e in strList:
        key = ''.join(sorted(e))
        if key not in anagrams.keys():
            anagrams[key] = [e]
        else:
            anagrams[key].append(e)

    return [l for lst in anagrams.values() for l in lst]


print(grupAnagrams(s1))




