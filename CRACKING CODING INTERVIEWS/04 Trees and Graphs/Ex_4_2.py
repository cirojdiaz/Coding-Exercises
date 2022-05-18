from TreesGraphs import NodeTG, printTree
from StacksAndQueues import Queue


def fillTree(n):
    if len(n) == 0:
        return NodeTG()
    q = Queue()
    first = NodeTG(n.pop())
    first.addChild(NodeTG(n.pop()))
    first.addChild(NodeTG(n.pop()))
    q.add(first)
    while not q.isEmpty():
        topNode = q.remove()
        for node in topNode.children:
            if not len(n) == 0:
                node.addChild(NodeTG(n.pop()))
                q.add(node)
            if not len(n) == 0:
                node.addChild(NodeTG(n.pop()))
                q.add(node)
    return first


numbers = list(range(20))
# numbers = []
t = fillTree(numbers)
print(printTree(t))
