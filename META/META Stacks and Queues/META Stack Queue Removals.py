import math


# Add any extra import statements you may need here


# Add any helper functions you may need here
class Node:
    def __init__(self, elm=None, pos=None):
        self.value = [elm, pos]


class Queue:
    def __init__(self, arr):
        if type(arr) is not Node:
            self.first = Node(arr[0], 0)
            self.last = self.first
            self.size = 1
            for elm, pos in zip(arr[1:], range(1, len(arr))):
                node = Node(elm, pos)
                self.last.next = node
                self.last = node
                self.size += 1
        else:
            self.first = arr
            self.last = self.first
            self.size = 1

    def dequeue(self):
        self.size -= 1
        node = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return node

    def enqueue(self, node: Node):
        if self.size == 0:
            self.first = node
            self.last = node
        else:
            node.next = None
            self.last.next = node
            self.last = node
        self.size += 1


# Let us use list as stack
def findPositions(a, x: int):
    arr = Queue(a)
    output = []
    for _ in range(x):
        maximum = arr.dequeue()
        queue = Queue(maximum)
        N = arr.size+1
        for k in range(1, min(x, N)):
            queue.enqueue(arr.dequeue())
            if queue.last.value[0] > maximum.value[0]:
                maximum = queue.last
        for k in range(queue.size):
            node = queue.dequeue()
            if not node == maximum:
                node.value[0] -= node.value[0] > 0
                arr.enqueue(node)
            else:
                output.append(node.value[1]+1)
    return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')


def printIntegerList(array):
    size = len(array)
    print('[', end='')
    for i in range(size):
        if i != 0:
            print(', ', end='')
        print(array[i], end='')
    print(']', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    expected_size = len(expected)
    output_size = len(output)
    result = True
    if expected_size != output_size:
        result = False
    for i in range(min(expected_size, output_size)):
        result &= (output[i] == expected[i])
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printIntegerList(expected)
        print(' Your output: ', end='')
        printIntegerList(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    n_1 = 6
    x_1 = 5
    arr_1 = [1, 2, 2, 3, 4, 5]
    expected_1 = [5, 6, 4, 1, 2]
    output_1 = findPositions(arr_1, x_1)
    check(expected_1, output_1)

    n_2 = 13
    x_2 = 4
    arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
    expected_2 = [2, 5, 10, 13]
    output_2 = findPositions(arr_2, x_2)
    check(expected_2, output_2)

    # Add your own test cases here
