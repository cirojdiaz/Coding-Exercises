from LinkedList import SLinkedList, Node

lst_link = SLinkedList('1')

lst_link.append('1')
lst_link.append('3')
lst_link.append('1')
lst_link.append('2')

lst_link.delete_value('1')
lst_link.listprint()
