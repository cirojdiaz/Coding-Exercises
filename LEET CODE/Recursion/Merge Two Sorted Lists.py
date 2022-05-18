"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toList(self):
        lst = []
        this = self
        while this is not None:
            lst.append(this.val)
            this = this.next
        return lst


def mergeTwoLists(list1, list2):
    root1 = ListNode(list1[0])
    root2 = ListNode(list2[0])
    this1, this2 = root1, root2
    for l1 in list1[1:]:
        this1.next = ListNode(l1)
        this1 = this1.next
    for l2 in list2[1:]:
        this2.next = ListNode(l2)
        this2 = this2.next

    def filRecursive(l1, l2):
        if l1 and l2:
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                node.next = filRecursive(l1.next, l2)
            else:
                node = ListNode(l2.val)
                node.next = filRecursive(l1, l2.next)
        elif l1:
            node = ListNode(l1.val)
            node.next = filRecursive(l1.next, l2)
        elif l2:
            node = ListNode(l2.val)
            node.next = filRecursive(l1, l2.next)
        else:
            return None

        return node

    return filRecursive(root1, root2)



list1 = [1, 2, 4]
list2 = [1, 3, 4]
Output = [1, 1, 2, 3, 4, 4]
print(Output)
print(mergeTwoLists(list1, list2).toList())
