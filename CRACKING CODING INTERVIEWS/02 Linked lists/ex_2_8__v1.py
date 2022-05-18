from LinkedList import SLinkedList, Node


# Create Circular list

def define_list():
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
    return lst


lst = define_list()


def loop_detected(lst: SLinkedList):
    slower = lst.headval.nextval
    faster = lst.headval.nextval.nextval
    # Detect colision point
    while faster is not None and faster != slower:
        slower = slower.nextval
        faster = faster.nextval.nextval
    if faster is None:
        return faster
    slower = lst.headval
    while slower != faster:
        slower = slower.nextval
        faster = faster.nextval
    return slower


try:
    print(loop_detected(lst).dataval)
except:
    print("Not Loop")
