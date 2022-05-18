# Random Node: You are implementing a binary tree class from scratch which, in addition to
# insert, find, and delete, has a method getRandomNodeQ which returns a random node
# from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
# for get RandomNode, and explain how you would implement the rest of the methods.
# Hints: #42, #54, #62, #75, #89, #99, #112, #119


from TreesGraphs import Node_Bin


# NOT FINISHED
class NodeTree(Node_Bin):
    def __init__(self, value=None, left=None, right=None):
        super().__init__(value=value, left=left, right=right)
        self.size = 0

    def getRandom(self):
        pass

    def insert(self, nd: float):
        if self.value >= nd:
            if self.left is None:
                self.left = NodeTree(nd)
            else:
                self.left.insert(nd)
        else:
            if self.right is None:
                self.right = NodeTree(nd)
            else:
                self.right.insert(nd)
        self.size += 1

    def find(self):
        pass


n = NodeTree()
