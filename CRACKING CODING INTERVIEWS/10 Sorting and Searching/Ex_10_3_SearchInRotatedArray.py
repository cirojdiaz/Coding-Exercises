# Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may assume that the array was
# originally sorted in increasing order.
# EXAMPLE
# Input:find5in{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
# Output: 8 (the index of 5 in the array)
# Hints: #298, #310


arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]


# arr = [15, 16, 19, 20, 25, 26, 1, 2, 3]

# Solution 1 Bad: exhaustive Search
def straightSearch(a: list, e: int):
    pos = 0
    while not a[pos] == e:
        pos += 1
    return pos


# Solution 2: Find th breaking point, reorder the array, do binary search
def breakPosition(a):
    if len(a) == 1:
        return None
    mid = len(a) // 2
    if a[mid - 1] > a[mid]:
        return mid
    left = breakPosition(a[:mid])
    if left is not None:
        return left
    else:
        right = breakPosition(a[mid:])
        if right is not None:
            return right + mid
    return None

def findInSortedArray(nums, n):

    def SortedBinarySearch(low, high):
        if high >= low:
            mid = (high + low) // 2
            if nums[mid] == n:
                return mid
            if nums[mid] < n:
                return SortedBinarySearch(mid, high)
            return SortedBinarySearch(low, mid)
        return -1
    return SortedBinarySearch(0, len(nums))

bpos = breakPosition(arr)
new = arr[bpos:] + arr[:bpos]
print('The original array was: \n{}'.format(arr))
print(f'The new array is \n {new}')
pos = findInSortedArray(new, 7)
print(f'The position in the original array is: \n {pos+bpos} \n')


# Solution 3: extended array
print('The original array was: \n{}'.format(arr))
print(f'The extended array is: \n{arr + arr + arr}')
pos = findInSortedArray(arr + arr + arr, 7) % len(arr)
print(f'The position is : \n{pos}')
