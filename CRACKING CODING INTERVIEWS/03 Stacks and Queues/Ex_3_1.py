from StacksAndQueues import Stack, Queue

s = Stack()

for k in range(10):
    s.push(val=k)

print(s.to_list())

q = Queue()

for k in range(10):
    q.add(val=k)

print(q.to_list())


