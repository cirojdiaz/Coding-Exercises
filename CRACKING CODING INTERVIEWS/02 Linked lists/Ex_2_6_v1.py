from LinkedList import Node, SLinkedList

# word = SLinkedList(['m', 'n', 'j', 'n', 'm'])
word = SLinkedList(['m', 'n', 'j', 'j', 'n', 'm'])


def is_palindrom(w: SLinkedList):
    fast = w.headval
    slow = w.headval
    stack = []
    while fast is not None and fast.nextval is not None:
        stack.append(slow.dataval)
        slow = slow.nextval
        fast = fast.nextval.nextval
    if fast is not None:
        slow = slow.nextval
    while slow is not None:
        if slow.dataval != stack.pop():
            return False
        slow = slow.nextval
    return True

print(is_palindrom(word))