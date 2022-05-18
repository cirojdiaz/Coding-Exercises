# Sort stack

from StacksAndQueues import Stack
from LinkedList import Node


def SortStack(s: Stack):
    s_sorted = Stack()
    while not s.isEmpty():
        tmp = s.pop().dataval
        while not s_sorted.isEmpty() and s_sorted.peek().dataval > tmp:
            s.push(s_sorted.pop().dataval)
        s_sorted.push(tmp)
    while not s_sorted.isEmpty():
        s.push(s_sorted.pop().dataval)


s = Stack()
for k in [5,3,4,1,2]:
    s.push(k)

print(s.to_list())
SortStack(s)
print(s.to_list())