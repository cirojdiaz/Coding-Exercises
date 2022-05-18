from LinkedList import SLinkedList, Node

# Create Circular list

len = 10
loop_pos = 5
val = list(range(len))
lst = SLinkedList(val)
n = lst.headval
for k in range(len - 1):
    if k == loop_pos:
        n_loop = n
    n = n.nextval
n.nextval = n_loop


def loop_detect(lst: SLinkedList):
    buffer = set()
    n = lst.headval
    while n is not None and n not in buffer:
        buffer.add(n)
        n = n.nextval
    return n


try:
    print(loop_detect(lst=lst).dataval)
except:
    print('None')
