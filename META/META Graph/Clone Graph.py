# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
# For simplicity, each node's value is the same as the node's index (1-indexed).
# For example, the first node with val == 1, the second node with val == 2, and so on.
# The graph is represented in the test case using an adjacency list.

from collections import deque


class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    curr = Node(node.val, node.neighbors)
    visited = {curr.val}
    queue = deque([curr])
    adjList = []

    while queue:

        curr = queue.popleft()
        neighList = [curr.val, []]
        for n in curr.neighbors:
            neighList[1].append(n.val)
            if n.val not in visited:
                nCopy = Node(n.val, n.neighbors)
                visited.add(nCopy.val)
                queue.append(nCopy)
        adjList.append(neighList)

    return [l[1] for l in adjList]


adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)

a1.neighbors = [a2, a4]
a2.neighbors = [a1, a3]
a3.neighbors = [a2, a4]
a4.neighbors = [a1, a3]

print(cloneGraph(a1))
