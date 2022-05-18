# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.


from TreesGraphs import Node_Bin, builtFromDict


def successor(root: Node_Bin, val):
    this = root
    old = Node_Bin()
    while this.value != val:
        if val < this.value:
            old = this
            if this.left is None:
                return None
            this = this.left
        else:
            if this.right is None:
                return None
            this = this.right
            if this.right is not None and val >= this.right.value:
                old = this
    return old.value


root = builtFromDict(root_val=4, children=[[2, [[1, None], [3, [[2.5, None], [3.5, None]]]]], [5, None]])
print(successor(root, 3))