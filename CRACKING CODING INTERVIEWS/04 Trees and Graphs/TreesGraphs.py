# 04 Trees and Graphs
import random
from StacksAndQueues import Queue


class NodeTG:
    def __init__(self, value=None, children=None):
        self.value = value
        self.state = None
        if children is not None:
            self.children = children
        else:
            self.children = []

    def addchidren(self, children):
        self.children = children

    def addChild(self, n):
        self.children.append(n)


class graph:
    def __init__(self, nodes=None):
        if type(nodes) is dict:
            s = dict()
            for k in nodes.keys():
                s[k] = NodeTG(k)
            for node, lst in zip(s.values(), nodes.values()):
                node.addchidren([s[k] for k in lst if k is not None])
            self.nodes = list(s.values())
        else:
            self.nodes = nodes

    def to_dict(self):
        dct = dict()
        for node in self.nodes:
            dct[node.value] = [n.value for n in node.children]
        return dct

    def adjacency(self):
        return []


class Node_Bin:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        if left is not None:
            self.left = Node_Bin(value=left)
        else:
            self.left = left
        if right is not None:
            self.right = Node_Bin(value=right)
        else:
            self.right = right


def builtFromDict(root_val, children):
    if root_val is None:
        return None
    root = Node_Bin(root_val)
    if children is not None:
        root.left = builtFromDict(children[0][0], children[0][1])
        root.right = builtFromDict(children[1][0], children[1][1])
    else:
        root.left = None
        root.right = None
    return root


def listOfDepthsGT_Breadth(root: NodeTG):
    Levels_lst = []
    CurrentLevel_lst = [root]
    while len(CurrentLevel_lst) != 0:
        Levels_lst.append(CurrentLevel_lst)
        CurrentLevel_lst = []
        for node in Levels_lst[-1]:
            if len(node.children) != 0:
                for n in node.children:
                    CurrentLevel_lst.append(n)
    return Levels_lst


def listOfDepthsBinary_Breadth(root: Node_Bin):
    Levels_lst = []
    CurrentLevel_lst = [root]
    while len(CurrentLevel_lst) != 0:
        Levels_lst.append(CurrentLevel_lst)
        CurrentLevel_lst = []
        for node in Levels_lst[-1]:
            children = [n for n in [node.left, node.right] if n is not None]
            for n in children:
                CurrentLevel_lst.append(n)
    return Levels_lst


def binaryToGeneralTree(root: Node_Bin):
    if root is None:
        return None
    node = NodeTG()
    node.value = root.value
    left = binaryToGeneralTree(root.left)
    right = binaryToGeneralTree(root.right)
    if left is not None and right is not None:
        node.children = [left, right]
    else:
        node.children = []
    return node


def printTree(root: NodeTG):
    q = Queue()
    q.add(root)
    L = [root.value]
    while not q.isEmpty():
        n = q.remove()
        for c in n.children:
            q.add(c)
            L.append(c.value)
    return L


def transversalListFill(arr: list):
    root = Node_Bin(arr.pop())

    def preOrderTransversal(r: Node_Bin):
        if arr[-1] <= r.value:
            if r.left is None:
                r.left = Node_Bin(arr.pop())
                return
            preOrderTransversal(r.left)
        elif arr[-1] > r.value:
            if r.right is None:
                r.right = Node_Bin(arr.pop())
                return
            preOrderTransversal(r.right)

    while not len(arr) == 0:
        preOrderTransversal(root)
    return root


def builtGraph(nnodes=10):
    s = []
    for k in range(nnodes):
        s.append(NodeTG(k))
    for node in s:
        ch = {random.randint(0, nnodes - 1) for _ in range(random.randrange(1, 3))}
        node.addchidren([s[_] for _ in ch])
    return graph(s)

# Prior to your interview, you should be comfortable implementing in-order, post-order, and pre-order
# traversal.The most common of these is in-order traversal.

# n = NodeTG()

# def inOrderTransversal(nd: NodeTG):
#     if nd is not None:
#         inOrderTransversal(nd.left)
#         visit(nd)
#         inOrderTransversal(nd.right)
#
#
# def preOrderTransversal(nd: NodeTG):
#     if nd is not None:
#         visit(nd)
#         inOrderTransversal(nd.left)
#         inOrderTransversal(nd.right)
#
#
# def postOrderTransversal(nd: NodeTG):
#     if nd is not None:
#         inOrderTransversal(nd.left)
#         inOrderTransversal(nd.right)
#         visit(nd)
