# Validate BST: Implement a function to check if a binary tree is a binary search tree.

from TreesGraphs import Node_Bin, builtFromDict


def isBST(root: Node_Bin, Min, Max):

    if root is None:
        return True

    # Current value needs to be in the interval
    if (Min is not None and root.value <= Min) or (Max is not None and root.value > Max):
        return False

    # Left and right trees needs to be BST
    if not isBST(root.left, Min, root.value) or not isBST(root.right, root.value, Max):
        return False

    return True


root = builtFromDict(root_val=4, children=[[2, [[1, None], [3, None]]], [5, None]])
print(isBST(root, None, None))
