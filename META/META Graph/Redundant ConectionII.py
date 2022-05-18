# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root)
# for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
# The given input is a directed graph that started as a rooted tree with n nodes (with distinct values from 1 to n),
# with one additional directed edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [ui, vi] that represents a directed edge
# connecting nodes ui and vi, where ui is a parent of child vi.
# Return an edge that can be removed so that the resulting graph is a rooted tree of n nodes. If there are multiple answers,
# return the answer that occurs last in the given 2D-array.

# In this problem, a tree is an undirected graph that is connected and has no cycles.
# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
# The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
# The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
# Return an edge that can be removed so that the resulting graph is a tree of n nodes.
# If there are multiple answers, return the answer that occurs last in the input.

from collections import defaultdict, deque


def findRedundantDirectedConnection(edges):

    # find the head
    parents, children = {e[0] for e in edges}, {e[1] for e in edges}
    if not (parents-children):
        head = 1
    else:
        head = (parents-children).pop()
    headers, others = [], []
    for e in edges:
        if e[0] == head: headers.append(e)
        else: others.append(e)
    edges = headers + others

    graph = defaultdict(deque)
    for i, j in edges: graph[i].append(j)

    queue = deque([head])
    visited = {head}
    while queue:
        this = queue.popleft()

        for node in graph[this]:
            if node in visited:
                lastOne = (this, node)
                break
            queue.append(node)
            visited.add(node)

    for e in edges:
        if e[0] == head:
            if e[1] == lastOne[1]:
                return e
        else: return lastOne




edges = [[1,2],[1,3],[2,3]]
# edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
# edges = [[2,1],[3,1],[4,2],[1,4]]
# edges = [[5,2],[5,1],[3,1],[3,4],[3,5]]
print(findRedundantDirectedConnection(edges))
# print(expected)
