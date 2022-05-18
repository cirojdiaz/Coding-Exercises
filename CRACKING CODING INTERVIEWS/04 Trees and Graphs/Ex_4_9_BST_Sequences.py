# BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.

from TreesGraphs import Node_Bin, transversalListFill, binaryToGeneralTree, listOfDepthsBinary_Breadth

# an array that gives the same tree is any permutation of the levels.
BSTLevelPermutations = []


def permutations(lst: list):
    N = len(lst)
    L = set(lst)
    permut = []

    def permute(this_list: set):
        if len(this_list) == 0:
            return []
        for v in this_list:
            this_perm = [v.value] + permute(this_list - {v})
            if len(this_list) == N:
                permut.append(this_perm)
        return this_perm

    permute(L)
    return permut


def numPermutations(thisList: list):
    this = []
    if len(thisList) == 1:
        return [[n] for n in range(thisList[0])]
    for j in range(thisList[0]):
        for lst in numPermutations(thisList[1:]):
            this.append([j] + lst)
    return this


lst = [5, 80, 65, 15, 10, 70, 25, 20, 60, 50]
root = transversalListFill(lst)

# Do a list of Depth version for binary trees.
L = listOfDepthsBinary_Breadth(root)
for subList in L:
    print([n.value for n in subList])

for l in L:
    BSTLevelPermutations.append(permutations(l))

# get index permutations
lens = [len(_) for _ in BSTLevelPermutations]

p = numPermutations(lens)
ej_num = p[4]

ej_list = []
for lev in range(len(BSTLevelPermutations)):
    ej_list += BSTLevelPermutations[lev][ej_num[lev]]

ej_list.reverse()
print(ej_list)

newRoot = transversalListFill(ej_list)
L = listOfDepthsBinary_Breadth(newRoot)
for subList in L:
    print([n.value for n in subList])
