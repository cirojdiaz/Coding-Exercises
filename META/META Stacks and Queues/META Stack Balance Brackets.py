import math

# Add any extra import statements you may need here


# Add any helper functions you may need here


class Node:
    def __init__(self, v):
        self.value = v
        self.next: None


class Stack:
    def __init__(self):
        self.last = None

    def peek(self):
        return self.last

    def pop(self):
        node = self.last
        self.last = self.last.next
        return node

    def push(self, val):
        node = Node(val)
        node.next = self.last
        self.last = node


def isBalanced(s):
    if not s:
        return True
    stack = Stack()
    stack.push(s[0])
    closed = {')', ']', '}'}
    opened = {'(', '[', '{'}
    tups = {('(', ')'), ('[', ']'), ('{', '}')}
    for e in s[1:]:
        if e in opened:
            stack.push(e)
        elif (stack.peek().value, e) in tups:
            stack.pop()
        elif e in closed:
            return False
        else:
            stack.push(e)
    if stack.last is None:
        return True
    return False


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    s1 = "{[(])}"
    expected_1 = False
    output_1 = isBalanced(s1)
    check(expected_1, output_1)

    s2 = "{{[[(())]]}}"
    expected_2 = True
    output_2 = isBalanced(s2)
    check(expected_2, output_2)

    s3 = "([{()}][])"
    expected_3 = True
    output_3 = isBalanced(s3)
    check(expected_3, output_3)

    # Add your own test cases here
