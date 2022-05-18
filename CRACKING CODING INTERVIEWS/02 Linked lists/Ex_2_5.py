import random

from LinkedList import Node, SLinkedList

# Rev1 = SLinkedList()
# Rev1.headval = NodeTG(random.randrange(0,9))
# for k in [random.randrange(1,9) for _ in range(6)]:
#     Rev1.append(k)
#
# Rev2 = SLinkedList()
# Rev2.headval = NodeTG(random.randrange(0,9))
# for k in [random.randrange(1, 9) for _ in range(6)]:
#     Rev2.append(k)

Rev1 = SLinkedList([2, 7, 7, 6, 2, 7, 6])
Rev2 = SLinkedList([8, 2, 5, 2, 4, 4, 4, 1,9])

print(Rev1.to_list())
print(Rev2.to_list())


def sum_lst(L1:SLinkedList, L2: SLinkedList):
    t1, t2 = L1.headval, L2.headval
    sum, times = 0, 0
    dec = 1
    while t1 is not None and t2 is not None:
        times, rest = divmod((t1.dataval + t2.dataval + times), 10)
        sum += dec * rest
        t1 = t1.nextval
        t2 = t2.nextval
        dec *= 10
    while t1 is not None:
        sum += (t1.dataval + times) * dec
        times = 0
        t1 = t1.nextval
        dec *= 10
    while t2 is not None:
        sum += (t2.dataval + times) * dec
        times = 0
        t2 = t2.nextval
        dec *= 10
    sum += dec * times
    return sum

print('\n')
print(sum_lst(Rev2, Rev1))