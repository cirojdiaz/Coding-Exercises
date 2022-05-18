# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.


from TreesGraphs import Node_Bin, builtFromDict, printTree, binaryToGeneralTree, listOfDepthsGT_Breadth
from StacksAndQueues import Queue



def findPath(root: Node_Bin, node: Node_Bin):
    # Perform a transversal-first-search until finding node
    Path = []

    def transSearch(r: Node_Bin):
        if r is None:
            return
        Path.append(r)  # r is a possible step in the path to node
        if not r == node:
            transSearch(r.left)
            if Path[-1] == node:    # if you found it do not look anymore
                return
            transSearch(r.right)
            if Path[-1] == node:    # if you found it do not look anymore
                return
            Path.pop()

    transSearch(root)
    return Path


Tree_lst = [4, [[2, [[1, None], [3, [[2.5, None], [3.5, None]]]]], [5, None]]]
root = builtFromDict(root_val=Tree_lst[0], children=Tree_lst[1])

LT = listOfDepthsGT_Breadth(binaryToGeneralTree(root))
for lt in LT:
    print([n.value for n in lt])

n1 = root.left.right.left
n2 = root.right
L1 = findPath(root, n1)
L2 = findPath(root, n2)

print([node.value for node in L1])
print([node.value for node in L2])

# Look for the intersection point
