# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.
# Hints: #332


A = [3, 6, 8, 22, 33, 44, 55, 66, 0, 0, 0, 0, 0, 0]
B = [5, 9, 32, 44, 51, 52]


def sortedMerge(A: list, B: list):
    indexB = len(B) - 1
    indexA = 8 - 1
    last = len(A) - 1
    while not indexB == -1:
        if A[indexA] > B[indexB]:
            A[last] = A[indexA]
            indexA -= 1
        else:
            A[last] = B[indexB]
            indexB -= 1
        last -= 1


print(A)
print(B)
sortedMerge(A, B)
print(A)
