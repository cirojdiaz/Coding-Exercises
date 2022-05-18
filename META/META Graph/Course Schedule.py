# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


from collections import deque
from collections import defaultdict


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    # We need to detect if there are loops. If not loops then we can do all courses.
    requiredCurses = [0] * numCourses
    dict1 = defaultdict(list)

    for i, j in prerequisites:
        requiredCurses[i] += 1
        dict1[j].append(i)

    notRequiredCourse = [idx for idx, v in enumerate(requiredCurses) if v == 0]

    while notRequiredCourse:
        v = notRequiredCourse.pop()
        for u in dict1[v]:
            requiredCurses[u] -= 1
            if requiredCurses[u] == 0:
                notRequiredCourse.append(u)

    return not any(requiredCurses)


# numCourses = 2
# prerequisites = [[1, 0], [0, 1]]

numCourses = 7
prerequisites = [[1, 0], [2, 1], [3, 2], [6, 4]]

print(canFinish(numCourses, prerequisites))
