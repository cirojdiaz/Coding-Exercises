# Remove Dupsr Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
# Hints: #9, #40 


from LinkedList import Node, SLinkedList

# LL = SLinkedList(random.randrange(0, 9))
# for k in range(20):
#     LL.append(random.randrange(0, 9))

LL = SLinkedList('1')
LL.append('1')
LL.append('2')
LL.append('3')
LL.append('4')
LL.append('3')

LL.listprint()


def remove_dup(lst: SLinkedList, buffer=True):
    if buffer:
        repeted = set()
        this = lst.headval
        previous = Node
        while this is not None:
            if this.dataval in repeted:
                previous.nextval = this.nextval
            else:
                repeted.add(this.dataval)
                previous = this
            this = this.nextval
    else:
        this = lst.headval
        while this is not None:
            runer = this
            while runer.nextval is not None:
                if runer.nextval.dataval == this.dataval:
                    runer.nextval = runer.nextval.nextval
                else:
                    runer = runer.nextval
            this = this.nextval
    return lst


LL = remove_dup(LL, buffer=False)
print('New list')
LL.listprint()
