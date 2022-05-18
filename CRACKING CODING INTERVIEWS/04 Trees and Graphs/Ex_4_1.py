# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes,

# This problem can be solved by just simple graph traversal such as depth-first search or breadth-first search.
# We start with one of the two nodes and, during traversal check if the other node is found. We should mark
# any node found in the course of the algorithm as "already visited" to avoid cycles and repetition of the
# nodes.

from TreesGraphs import graph, builtGraph, NodeTG
import random
from StacksAndQueues import Queue


class NodeState:
    def __init__(self):
        self.Unvisited = 'Unvisited'
        self.Visited = 'Visited'
        self.Visiting = 'Visiting'


def thereIsPath(g: graph, start: NodeTG, end: NodeTG):
    State = NodeState()
    if start == end:
        return True
    q = Queue()

    for u in g.nodes:
        u.state = State.Unvisited

    start.state = State.Visiting
    q.add(start)
    while not q.isEmpty():
        u = q.remove()
        if u is not None:
            for v in u.children:
                if v.state == State.Unvisited:
                    if v == end:
                        return True
                    else:
                        v.state = State.Visiting
                        q.add(v)
            u.state = State.Visiting
    return False


g = builtGraph(10)
# g = graph({0: [0, 5], 1: [1], 2: [6], 3: [4, 6], 4: [9], 5: [0, 1], 6: [0], 7: [3, 4], 8: [2, 4], 9: [5]})

print(g.to_dict())

# Select wo nodes
n1 = g.nodes[random.randint(0, len(g.nodes) - 1)]
n2 = g.nodes[random.randint(0, len(g.nodes) - 1)]
# n1 = g.nodes[2]
# n2 = g.nodes[9]

print('Nodes {} and {}'.format(n1.value, n2.value))

print('there is {} a path'.format('Not' * (not thereIsPath(g, n1, n2))))
