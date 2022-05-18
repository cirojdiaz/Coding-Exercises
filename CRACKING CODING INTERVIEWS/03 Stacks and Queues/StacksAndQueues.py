# 03 Stacks and Queues
from LinkedList import SLinkedList, Node


class Stack:
    def __init__(self, val=None):
        if val is None:
            self.head = None
            self.size = 0
        else:
            self.head = Node(val)
            self.size = 1

    def push(self, val):
        ## LIFO
        if self.head is None:
            self.head = Node(val)
        else:
            n = Node(val)
            n.nextval = self.head
            self.head = n
        self.size += 1

    def pop(self):
        n = self.head
        self.head = self.head.nextval
        self.size -= 1
        return n

    def peek(self):
        return self.head

    def size(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def to_list(self):
        l = []
        n = self.head
        while n is not None:
            l.append(n.dataval)
            n = n.nextval
        return l


class Queue:
    def __init__(self, val=None):
        if val is None:
            self.head = None
            self.last = None
            self.size = 0
        else:
            self.head = Node(val)
            self.last = self.head
            self.size = 1

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
            self.last = self.head
            self.size = 1
        else:
            n = Node(val)
            self.last.nextval = n
            self.last = n

    def remove(self):
        self.head = self.head.nextval

    def peek(self):
        return self.head

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def to_list(self):
        l = []
        n = self.head
        while n is not None:
            l.append(n.dataval)
            n = n.nextval
        return l







