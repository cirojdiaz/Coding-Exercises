# Recursive
def mergeSortRecursive(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSortRecursive(left)
        mergeSortRecursive(right)

        # Two iterators for traversing the two halves
        i, j = 0, 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


# Iterative
def mergeSortIterative(arr):
    switcher = [arr, arr.copy()]
    active, passive = 0, 1

    def merge(l1, r1, l2, r2):
        p = l1
        while l1 <= r1 and l2 <= r2:
            if switcher[passive][l1] <= switcher[passive][l2]:
                switcher[active][p] = switcher[passive][l1]
                l1 += 1
            else:
                switcher[active][p] = switcher[passive][l2]
                l2 += 1
            p += 1

        while l1 <= r1:
            switcher[active][p] = switcher[passive][l1]
            l1 += 1
            p += 1

        while l2 <= r2:
            switcher[active][p] = switcher[passive][l2]
            l2 += 1
            p += 1

    # Initialize pairs
    LAST = len(arr) - 1
    for k in range(0, LAST, 2):
        if switcher[passive][k] > switcher[passive][k + 1]:
            switcher[active][k] = switcher[passive][k + 1]
            switcher[active][k + 1] = switcher[passive][k]

    level = 1

    while 2 ** level <= LAST:
        active = active == 0
        passive = passive == 0
        l1, r1, l2, r2 = 0, 2 ** level - 1, 2 ** level, min(2 ** level + 2 ** level - 1, LAST)

        while l1 < LAST:
            merge(l1, r1, l2, r2)
            l1 = l1 + 2 ** (level + 1)
            r1 = min(r1 + 2 ** (level + 1), LAST)
            l2 = l2 + 2 ** (level + 1)
            r2 = min(r2 + 2 ** (level + 1), LAST)
        level += 1

    return switcher[active]


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20, 1, 22, 44]
print(myList)
print(mergeSortIterative(myList))
