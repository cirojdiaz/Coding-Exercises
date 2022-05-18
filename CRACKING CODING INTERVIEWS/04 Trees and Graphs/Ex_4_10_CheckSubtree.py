# CheckSubtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
# algorithm to determine if T2 is a subtree of Tl.
# A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.

from TreesGraphs import transversalListFill, listOfDepthsBinary_Breadth, Node_Bin

l1 = [5, 80, 65, 15, 10, 70, 25, 20, 60, 50]
T1 = transversalListFill(l1.copy())

l2 = [5, 15, 10, 25, 20]
T2 = transversalListFill(l2.copy())


# Give us a list of the value of nodes while traversing the Tree in preorder
def traversalListChar(root: Node_Bin):
    listChar = []
    def transv(r: Node_Bin):
        if r is None:
            listChar.append(100)
            return
        listChar.append(r.value)
        transv(r.left)
        transv(r.right)

    transv(root)
    return listChar


# Check if L1 is in L2
def isContainedIn(short, big):
    pos = 0
    N = len(short)
    for v in big:
        if v == short[pos]:
            pos += 1
            if pos == N:
                return True
        else:
            pos = 0
    return False


LB = listOfDepthsBinary_Breadth(T1)
print('Dict 1')
for l in LB:
    print([node.value for node in l])

LB = listOfDepthsBinary_Breadth(T2)
print('Dict 2')
for l in LB:
    print([node.value for node in l])

L1 = traversalListChar(T1)
print(L1)

L2 = traversalListChar(T2)
print(L2)

issublist = isContainedIn(L2, L1)
print(issublist)
