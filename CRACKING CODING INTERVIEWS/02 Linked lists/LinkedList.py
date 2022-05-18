class Node:
    def __init__(self, value=None, nextNode=None):
        self.dataval = value
        self.nextval = nextNode


class SLinkedList:
    def __init__(self, head=None):
        if type(head) is not list:
            self.headval = Node(head)
        else:
            self.headval = Node(head[0])
            this = self.headval
            for v in head[1:]:
                this.nextval = Node(v)
                this = this.nextval

    def append(self, data):
        newNode = Node(data)

        if self.headval is None:
            self.headval = newNode
            return

        lastNode = self.headval
        while lastNode.nextval:
            lastNode = lastNode.nextval

        lastNode.nextval = Node(data)

    def listprint(self):
        print_val = self.headval
        print(print_val.dataval)
        while print_val.nextval:
            print_val = print_val.nextval
            print(print_val.dataval)

    def delete_value(self, val):
        this = self.headval
        while this.dataval == val:
            this = this.nextval
        self.headval = this

        while this.nextval:
            old = this
            this = this.nextval
            if this.dataval == val:
                old.nextval = this.nextval
                this = this.nextval

    def to_list(self):
        this = self.headval
        lst = [this.dataval]
        while this.nextval:
            this = this.nextval
            lst.append(this.dataval)
        return lst
