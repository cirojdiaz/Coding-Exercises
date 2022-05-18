# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
# From each cell, you can either move in four directions: left, right, up, or down.
# You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
#

from collections import defaultdict, deque


def longestIncreasingPath(matrix):
    n, m = len(matrix), len(matrix[0])
    adj = defaultdict(list)
    allKeys = set()
    maxPath = [[0 for j in range(m)] for i in range(n)]
    MAX = 1

    for i in range(n):
        for j in range(m):
            key = matrix[i][j]
            allKeys.add(key)
            adj[key].append([i, j])

    keys = list(sorted(allKeys, reverse=True))
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for k in keys:
        for a in adj[k]:
            maximum = 1
            for d in directions:
                next = [a[0] + d[0], a[1] + d[1]]
                if 0 <= next[0] < n and 0 <= next[1] < m:
                    if matrix[a[0]][a[1]] < matrix[next[0]][next[1]]:
                        maximum = max(maximum, 1 + maxPath[next[0]][next[1]])
            maxPath[a[0]][a[1]] = maximum
            MAX = max(MAX, maximum)

    return MAX

# matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
# matrix = [[7, 7, 5],[2, 4, 6],[8, 2, 0]]
matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],
          [39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],
          [60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],
          [99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],
          [119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],
          [139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
print(longestIncreasingPath(matrix))
