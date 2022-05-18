"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row.
Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
"""


def kthGrammar(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """

    def helper(n, k):
        if n == 1:
            return 0
        prev = helper(n - 1, (k+1) // 2)
        if prev == 0:
            return 1-k % 2
        else:
            return k % 2

    return helper(n, k)

ex = ['0', '01', '0110', '01101001']

print(kthGrammar(2,1))