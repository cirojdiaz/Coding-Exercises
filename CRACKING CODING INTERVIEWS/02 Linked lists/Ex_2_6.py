from LinkedList import Node, SLinkedList

word = SLinkedList(['m', 'n', 'j', 'n', 'm'])


def is_palindrom(w: SLinkedList):
    sub_w = SLinkedList()
    this = w.headval
    while this is not None:
        previous = sub_w.headval
        sub_w.headval = Node(this.dataval)
        sub_w.headval.nextval = previous
        this = this.nextval
    t1 = w.headval
    t2 = sub_w.headval
    while t1 is not None:
        if t1.dataval != t2.dataval:
            return False
        t1 = t1.nextval
        t2 = t2.nextval
    return True


print(is_palindrom(word))
