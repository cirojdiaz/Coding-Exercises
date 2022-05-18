# Que Animals Catas and dogs

from StacksAndQueues import Queue
import random


class animal:
    def __init__(self, type):
        self.type = type
        self.ord = None

    def getOrd(self, ord):
        self.ord = ord


class shelterQueue():
    def __init__(self):
        self.cats = Queue()
        self.dogs = Queue()
        self.ord = 0

    def addAnimal(self, a: animal):
        self.ord += 1
        a.getOrd(self.ord)
        if a.type == 'cat':
            self.cats.add(a)
        if a.type == 'dog':
            self.dogs.add(a)

    def popany(self):
        c = self.cats.peek()
        d = self.dogs.peek()
        if c.dataval.ord > d.dataval.ord:
            return self.dogs.remove()
        return self.cats.remove()

    def to_list(self):
        return [self.cats.to_list(), self.dogs.to_list()]


shelter = shelterQueue()
type = ['cat', 'dog']
t = [0, 0, 1, 1, 0, 1, 1, 0]
for n in range(8):
    shelter.addAnimal(animal(type[t[n]]))

shelter.popany()
shelter.popany()
shelter.popany()
shelter.popany()
shelter.popany()

print([a.ord for a in shelter.to_list()[0]], [b.ord for b in shelter.to_list()[1]])
