from LinkedList import Node, SLinkedList


def define_lists():
    l1 = SLinkedList([1, 1.5])
    l2 = SLinkedList(1)
    n1 = l1.headval
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

# Naive way
def intersection(l1: SLinkedList, l2: SLinkedList):
    n1, n2 = l1.headval, l2.headval
    while n1 is not None:
        while n2 is not  None:
            if n1 == n2:
                return n1
            n2 = n2.nextval
        n2 = l2.headval
        n1 = n1.nextval
    return None

try:
    print(intersection(l1, l2).dataval)
except:
    print(None)






