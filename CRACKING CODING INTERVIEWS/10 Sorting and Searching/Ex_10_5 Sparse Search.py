# Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a
# method to find the location of a given string.

def sparseSearch(arr, s):
    left = 0
    right = len(arr) - 1
    if arr[left] == s:
        return left
    if arr[right] == s:
        return right

    while left < right:
        mid = (left + right) // 2
        midL = mid
        midR = mid

        # Moving to left and right until finding the closer non-empty position
        while midR < right and midL > left and arr[midL] == "" and arr[midR] == "":
            midL += 1
            midR += 1
            if not arr[midL] == "":
                mid = midL
            elif not arr[midR] == "":
                mid = midR

        if arr[mid] == s:
            return mid
        elif arr[mid] < s:
            left = mid + 1
        else:
            right = mid - 1

    return -1


str = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
print(str)
print(sparseSearch(str, 'at'))
