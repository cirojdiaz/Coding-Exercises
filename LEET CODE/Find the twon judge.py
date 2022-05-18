# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

"""
def findJudge(n, trust):

    # Find the one that trust no one
    outer = {i for i in range(1, n + 1)}
    for e in trust:
        if e[0] in outer:
            outer.remove(e[0])

    # if there is no one trusting nobody there is no judge
    if not len(outer) == 1:
        return -1
    judge = [e for e in outer][0]

    # Check everybody trust the judge
    outer = {i for i in range(1, n + 1)}
    for e in trust:
        if e[1] == judge and e[0] in outer:
            outer.remove(e[0])

    if len(outer)==1:
        return judge
    return -1
"""

def findJudge(n, trust):
    howManyTrustMe = [0 for _ in range(n)]
    howManyMeTrust = [0 for _ in range(n)]

    for e in trust:
        howManyTrustMe[e[1]-1] += 1
        howManyMeTrust[e[0]-1] += 1

    for a, b, i in zip(howManyTrustMe, howManyMeTrust, range(1, n+1)):
        if b == 0 and a == n-1:
            return i
    return -1


# trust = [[1, 2],[2, 3]]
# trust = [[1, 2]]
trust = [[1,2], [2,3], [3,4], [1,5], [2,5], [3,5], [4,5]]
print(findJudge(5, trust))
