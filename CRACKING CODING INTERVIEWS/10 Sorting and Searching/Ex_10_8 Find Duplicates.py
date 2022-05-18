# Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000.The
# array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory
# available, how would you print all duplicate elements in the array?


def findDuplicates(arr):
    # 4 kb is lower than 32000. We can then create an array until 32000
    numFreq = [0 for _ in range(32000)]
    duplicates = set()
    for a in arr:
        numFreq[a] += 1
        if numFreq[a] > 1:
            duplicates.add(a)

    return duplicates


arr = [2, 88, 88, 109, 3000, 3001, 2, 53, 88, 99]
print(arr)
print(findDuplicates(arr))
