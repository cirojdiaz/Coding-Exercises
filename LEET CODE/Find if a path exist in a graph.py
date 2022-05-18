# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
# The edges in the graph are represented as a 2D integer array edges,
# where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
# Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

from collections import deque


def validPath(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """

    conect = [[] for _ in range(n)]
    for e in edges:
        conect[e[0]].append(e[1])
        conect[e[1]].append(e[0])

    curr = source
    queue = deque([curr])
    visited = {curr}

    while queue:

        curr = queue.popleft()

        if curr == destination:
            return True

        for e in conect[curr]:
            if e not in visited:
                visited.add(e)
                queue.append(e)

    return False


# n = 3
# edges = [[0, 1],[1, 2],[2, 0]]
# source = 0
# destination = 2

# n = 6
# edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
# source = 0
# destination = 5

# n = 10
# edges = [[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]]
# source = 7
# destination = 5

# n = 10
# edges = [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]]
# source = 5
# destination = 9


n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5

print(validPath(n, edges, source, destination))
