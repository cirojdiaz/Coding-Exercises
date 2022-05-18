# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes.
# If there are multiple answers, return the answer that occurs last in the input.

from collections import defaultdict, deque


def findRedundantConnection(edges):
    graph = defaultdict(set)

    def dfsIter(source, target):
        stack = [source]
        seen = set()
        while stack:
            this = stack.pop()
            if this == target:
                return True
            if this not in seen:
                seen.add(this)
                for node in graph[this]:
                    stack.append(node)

    for u, v in edges:
        if u in graph and v in graph and dfsIter(u, v):
            return u, v
        graph[u].add(v)
        graph[v].add(u)


# edges = [[1, 2], [1, 3], [2, 3]]
# edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
edges = [[1, 3], [1, 2], [3, 5], [7, 6], [4, 7], [3, 4], [5, 6]]
# edges, expected = [[1,2],[2,3],[2,4],[4,5],[1,5]] , [1, 5]
# edges, expected = [[1,5],[3,4],[3,5],[4,5],[2,4]]  , [4,5]
# edges, expected  = [[1,2],[2,3],[1,5],[3,4],[1,4]] , [1,4]
# edges = [[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]
print(findRedundantConnection(edges))
# print(expected)
