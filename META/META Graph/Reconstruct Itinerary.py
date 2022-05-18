# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure
# and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK".
#     If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

from collections import defaultdict, deque


def findItinerary(tickets):
    tickets.sort()
    graph = defaultdict(deque)
    for s, f in tickets: graph[s].append(f)

    result = []
    stack = ['JFK']

    while stack:
        if graph[stack[-1]]:
            next = graph[stack[-1]].popleft()
            stack.append(next)
        else:
            result.append(stack.pop())
    return result[::-1]


# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets = [['JFK','A'], ['JFK','C'], ['C', 'B'], ['B', 'JFK']]
tickets = [["EZE", "TIA"], ["EZE", "HBA"], ["AXA", "TIA"], ["JFK", "AXA"], ["ANU", "JFK"], ["ADL", "ANU"],
           ["TIA", "AUA"], ["ANU", "AUA"], ["ADL", "EZE"], ["ADL", "EZE"], ["EZE", "ADL"], ["AXA", "EZE"],
           ["AUA", "AXA"], ["JFK", "AXA"], ["AXA", "AUA"], ["AUA", "ADL"], ["ANU", "EZE"], ["TIA", "ADL"],
           ["EZE", "ANU"], ["AUA", "ANU"]]
print(findItinerary(tickets))
