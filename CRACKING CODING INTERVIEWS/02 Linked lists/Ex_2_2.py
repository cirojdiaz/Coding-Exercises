from LinkedList import Node, SLinkedList

LL = SLinkedList('1')
LL.append('1')
LL.append('2')
LL.append('3')
LL.append('4')
LL.append('3')

LL.listprint()


def return_K_to_Last(lst: SLinkedList, k: int):
    this = lst.headval
    for c in range(k):
        if this is None:
            return None
        else:
            this = this.nextval
    lst.headval = this
    return lst


print('new:')
new_list = return_K_to_Last(LL, 10)
if new_list is not None:
    new_list.listprint()
else:
    print('No list to print')
