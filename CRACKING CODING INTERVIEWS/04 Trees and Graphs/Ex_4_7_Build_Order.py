# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.


from TreesGraphs import graph


def builtOrder(g: graph):
    Order = []
    notReferenced = set(g.nodes)
    while not len(notReferenced) == 0:
        referenced = set()
        for n in notReferenced:
            for c in n.children:
                referenced.add(c)
        for n in notReferenced.difference(referenced):
            notReferenced.remove(n)
            Order.append(n)
    return Order


dct = {'f': ['c', 'a', 'b'], 'c': ['a'], 'b': ['a', 'e'], 'a': ['e'], 'e': [None], 'd': ['g'], 'g': [None]}
g = graph(dct)
Order = builtOrder(g)
print([n.value for n in Order])