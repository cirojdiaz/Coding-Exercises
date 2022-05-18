from LinkedList import SLinkedList, Node


def define_lists():
    l1 = SLinkedList([1, 1.5])
    l2 = SLinkedList(1)
    n1 = l1.headval.nextval
    n2 = l2.headval
    for k in range(3):
        n1.nextval = Node(k)
        n2.nextval = Node(k*10)
        n1 = n1.nextval
        n2 = n2.nextval
    n3 = Node('Intersection')
    n1.nextval = n3
    n2.nextval = n3
    for k in range(100, 105):
        n3.nextval = Node(k)
        n3 = n3.nextval
    return l1, l2

l1, l2 = define_lists()
print(l1.to_list())
print(l2.to_list())


def intersection(lst1: SLinkedList, lst2: SLinkedList):
    n1, n2 = lst1.headval, lst2.headval
    len1, len2 = 0, 0
    while n1.nextval is not None:
        len1 += 1
        n1 = n1.nextval
    while n2.nextval is not None:
        len2 += 1
        n2 = n2.nextval
    if n1 != n2:
        return False
    n1, n2 = lst1.headval, lst2.headval
    # advance n1 or n2
    if len1 > len2:
        for _ in range(len1-len2):
            n1 = n1.nextval
    if len2 > len1:
        for _ in range(len2-len1):
            n2 = n2.nextval
    while n1 is not None:
        if n1 == n2:
            return n1
        n1 = n1.nextval
        n2 = n2.nextval
    return False

try:
    print(intersection(l1, l2).dataval)
except:
    print(None)





