from LinkedList import Node, SLinkedList

LL = SLinkedList('1')
LL.append('1')
LL.append('2')
LL.append('3')
LL.append('4')
LL.append('3')
print(LL.to_list())

def partition(lst: SLinkedList, pos: int):
    L1 = SLinkedList()
    L1.headval = lst.headval
    L2 = SLinkedList()
    this = L1.headval
    for n in range(pos - 1):
        this = this.nextval
    L2.headval = this.nextval
    this.nextval = None
    return L1, L2


L1, L2 = partition(lst=LL, pos=3)
print('\n')
print(L1.to_list())
print('\n')
print(L2.to_list())
