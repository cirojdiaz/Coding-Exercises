from LinkedList import Node, SLinkedList
import random

LL = SLinkedList()
LL.headval = Node(random.randrange(0, 9))
for k in [random.randrange(1, 9) for _ in range(6)]:
    LL.append(k)
print(LL.to_list())


def partition(lst: SLinkedList, val: int):
    lower = SLinkedList()
    greater = SLinkedList()
    this = lst.headval
    while this is not None:
        if this.dataval < val:
            lower_next = Node(this.dataval)
            if lower.headval.dataval is None:
                lower.headval = lower_next
                previous = lower_next
            else:
                previous.nextval = lower_next
                previous = previous.nextval
        else:
            greater_head = Node(this.dataval)
            if greater.headval.dataval is None:
                greater.headval = greater_head
            else:
                greater_head.nextval = greater.headval
                greater.headval = greater_head
        this = this.nextval

    previous.nextval = greater.headval
    return lower


print('\n')
print(partition(LL, 4).to_list())
