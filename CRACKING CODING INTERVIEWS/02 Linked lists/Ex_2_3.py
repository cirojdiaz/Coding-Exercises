# Delete Midel NodeTG

from LinkedList import Node, SLinkedList

LL = SLinkedList('1')
LL.append('1')
LL.append('2')
LL.append('3')
LL.append('4')
LL.append('3')

LL.listprint()


def delete_node(lst: SLinkedList, val):
    if lst.headval == val:
        lst.headval = lst.nextval
    else:
        this = lst.headval
        while this.nextval is not None:
            if this.nextval.dataval == val:
                this.nextval = this.nextval.nextval
                return lst
            else:
                this = this.nextval


print('new')
delete_node(lst=LL, val='3').listprint()
