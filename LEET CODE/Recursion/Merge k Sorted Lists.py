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


def mergeKLists(lists):
    listRoot = []
    for subList in lists:
        head = ListNode(subList[0])
        this = head
        for l in subList[1:]:
            this.next = ListNode(l)
            this = this.next
        listRoot.append(head)

    def findMin(L):
        minimum = 10**5
        index = -1
        for i in range(len(lists)):
            if L[i] is not None and minimum > L[i].val:
                minimum = L[i].val
                index = i
        return index

    def mergeRec(L):
        i = findMin(L)
        if i < 0:
            return None
        node = ListNode(L[i].val)
        L[i] = L[i].next
        node.next = mergeRec(L)
        return node

    return mergeRec(listRoot)


lists = [[1, 3, 4, 6, 8, 9, 12], [1, 2, 5, 7, 11, 21, 24], [-4, 0, 4, 7, 10, 14, 22, 29]]
Output = [-4, 0, 1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 14, 21, 22, 24, 29]
print(Output)
print(mergeKLists(lists).toList())
