# Random Node: You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNodeQ which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for get RandomNode, and explain how you would implement the rest of the methods.
# Hints: #42, #54, #62, #75, #89, #99, #112, #119

from TreesGraphs import Node_Bin, transversalListFill
import random


class Bin_Tree_Mod:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        self.treeSize()

    def treeSize(self):
        def preOrderTraversal(r: Node_Bin):
            if r is None:
                return
            self.size += 1
            preOrderTraversal(r.left)
            preOrderTraversal(r.right)
        preOrderTraversal(self.root)

    def preOrderTraversalList(self):
        lst = []

        def preordIt(r: Node_Bin):
            if r is None:
                return
            lst.append(r.value)
            preordIt(r.left)
            preordIt(r.right)

        return lst

    def getRandomNode(self):
        k = random.randint(0, self.size)
        node = self.root
        count = [0]

        def preOrderIt(r: Node_Bin):
            nonlocal node
            if r is None:
                return
            count[0] += 1
            if count[0] == k:
                node = r
                return
            preOrderIt(r.left)
            preOrderIt(r.right)
        preOrderIt(node)
        return node


l1 = [5, 80, 65, 15, 10, 70, 25, 20, 60, 50]
T1 = transversalListFill(l1.copy())
BTM = Bin_Tree_Mod(T1)
print('size of the tree is {}'.format(BTM.size))
print(BTM.getRandomNode().value)