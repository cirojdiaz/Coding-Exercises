# Validate BST: Implement a function to check if a binary tree is a binary search tree.

from TreesGraphs import Node_Bin, builtFromDict


def isBST(root: Node_Bin):
    if root is None:
        return True

    if not isBST(root.left) or not isBST(root.right):
        return False

    if root.left is not None and root.right is not None:
        if root.left.value > root.value or root.right.value <= root.value:
            return False
        else:
            return True
    else:
        return True


root = builtFromDict(root_val=4, children=[[2, [[1, None], [3, None]]], [5, None]])
print(isBST(root))
