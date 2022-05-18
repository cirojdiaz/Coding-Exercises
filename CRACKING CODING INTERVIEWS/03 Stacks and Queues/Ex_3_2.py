from StacksAndQueues import Stack
from LinkedList import SLinkedList, Node


class StackMin(Stack):
    def __init__(self, val=None):
        super().__init__(val)
        if val is None:
            self.minHead = None
        else:
            self.minHead = Node(val)

    def push(self, val):
        ## LIFO
        if self.head is None:
            self.head = Node(val)
            self.size = 1
            self.minHead = Node(val)
        else:
            n = Node(val)
            n.nextval = self.head
            self.head = n
            if self.minHead.dataval > val:
                m = Node(val)
            else:
                m = Node(self.minHead.dataval)
            m.nextval = self.minHead
            self.minHead = m

    def min(self):
        try:
            return self.minHead.dataval
        except:
            return None

    def pop(self):
        if self.head is not None:
            n = self.head
            self.head = self.head.nextval
            self.minHead = self.minHead.nextval
            self.size -= 1
        else:
            return None
        return n


s = StackMin()

for k in range(10, 0, -1):
    s.push(k)

for k in range(11):
    print(s.to_list())
    print(s.min())
    s.pop()
