# There is an undirected star graph consisting of n nodes labeled from 1 to n.
# A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi.
# Return the center of the given star graph.

def findCenter(edges):
    """
    :type edges: List[List[int]]
    :rtype: int
    """
    # Find the one
    theOne = -1
    for e1 in edges[0]:
        for e2 in edges[1]:
            if e1 == e2:
                theOne = e1
                break

    for e in edges[1:]:
        if theOne not in {e[0], e[1]}:
            return -1

    return theOne

edges = [[1,2],[5,1],[1,3],[1,4]]
print(findCenter(edges))