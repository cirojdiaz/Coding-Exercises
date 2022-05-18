# Given a binary tree, design an algorithm which creates a linked list of all the nodes
# at each depth

from TreesGraphs import NodeTG
from Ex_4_2 import fillTree
from LinkedList import SLinkedList


# This one using Breadth-first-Search
def ListOfDepths_Breadth(root: NodeTG):
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


# This using Traversal search (Recursive) THIS IS COMPLICATED TO LEARN
def ListOfDepths_Traversal(root: NodeTG, lists: list, level: int):
    if root is None:
        return
    lst = []
    if len(lists) == level:
        lists.append(lst)
    else:
        lst = lists[level]
    lst.append(root)
    for n in root.children:
        ListOfDepths_Traversal(n, lists, level+1)


numbers = list(range(20))
# numbers = []
t = fillTree(numbers)

LT = ListOfDepths_Breadth(t)

# LT = []
# ListOfDepths_Traversal(t, LT, 0)

for lt in LT:
    print([n.value for n in lt])
