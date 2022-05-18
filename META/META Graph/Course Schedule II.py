# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them.
# If it is impossible to finish all courses, return an empty array.


from collections import defaultdict


def findOrder(numCourses, prerequisites):
    """
    https://leetcode.com/problems/longest-increasing-path-in-a-matrix/submissions/
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """
    requiredCurses = [0] * numCourses
    dict1 = defaultdict(list)

    for i, j in prerequisites:
        requiredCurses[i] += 1
        dict1[j].append(i)

    notRequiredCourse = [idx for idx, v in enumerate(requiredCurses) if v == 0]
    path = []

    while notRequiredCourse:
        v = notRequiredCourse.pop()
        path.append(v)
        for u in dict1[v]:
            requiredCurses[u] -= 1
            if requiredCurses[u] == 0:
                notRequiredCourse.append(u)

    if not any(requiredCurses):
        return path

    return []

# numCourses = 2
# prerequisites = [[1, 0], [0, 1]]

numCourses = 7
prerequisites = [[1, 0], [2, 1], [3, 2], [6, 4]]

print(findOrder(numCourses, prerequisites))