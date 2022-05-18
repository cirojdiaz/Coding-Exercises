# Queue via Stack

from StacksAndQueues import Stack

class MyQueue:
    def __init__(self):
        self.stk_old = Stack()
        self.stk_new = Stack()

    def add(self, val):
        while not self.stk_old.isEmpty():
            self.stk_new.push(self.stk_old.pop().dataval)
        self.stk_new.push(val)

    def shiftStaks(self):
        if self.stk_old.isEmpty():
            while not self.stk_new.isEmpty():
                self.stk_old.push(self.stk_new.pop().dataval)

    def peek(self):
        self.shiftStaks()
        return self.stk_old.peek().dataval

    def remove(self):
        self.shiftStaks()
        return self.stk_old.pop().dataval

    def to_list(self):
        self.shiftStaks()
        return self.stk_old.to_list()

mq = MyQueue()
for j in range(5):
    mq.add(j)

print(mq.peek())
mq.remove()
print(mq.peek())




