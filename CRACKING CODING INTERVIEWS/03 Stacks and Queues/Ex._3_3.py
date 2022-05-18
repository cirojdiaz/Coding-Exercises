# Stack of plates

# from LinkedList import NodeTG, SLinkedList
from StacksAndQueues import Stack
import math


class SetOfStacks():

    def __init__(self, max=3):
        self.stacks = []
        self.max = max

    def push(self, val):
        if len(self.stacks) != 0 and self.stacks[-1].size < self.max:
            self.stacks[-1].push(val)
        else:
            self.stacks.append(Stack(val))

    def pop(self):
        if self.stacks[-1].size != 1:
            return self.stacks[-1].pop()
        else:
            return self.stacks.pop().pop()

    def popAt(self, stk):
        e = self.stacks[stk].pop()
        shift = None
        for s in self.stacks[-1:stk-1:-1]:
            old = None
            if shift is not None:
                s.push(shift)
            this = s.head
            while this.nextval is not None:
                old = this
                this = this.nextval
            shift = this.dataval
            if old is None:
                self.stacks.pop()
            elif s != self.stacks[stk]:
                old.nextval = None
        return e

    def to_list(self):
        lst = []
        for stk in self.stacks:
            lst.append(stk.to_list())
        return lst


S = SetOfStacks(max=3)
for k in range(15):
    S.push(k)

# for k in range(3):
#     S.pop()

print(S.to_list())
S.popAt(2)
print(S.to_list())
