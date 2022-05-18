# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
# steps at a time. Implement a method to count how many possible ways the child can run up the
# stairs.
# Hints: #152, #178, #217, #237, #262, #359



# Solution 1 (MINE)
def TripleStepRecursive(nSteps: int):
    ways = 0

    def iterative(steps):
        nonlocal ways
        if steps == nSteps:
            ways += 1
            return
        if steps > nSteps:
            return
        iterative(steps + 3)
        iterative(steps + 2)
        iterative(steps + 1)

    iterative(0)
    return ways


# Iterative Pending
def TripleStepIterative(nSteps: int):
    pass


# Solution 2
def countWaysRecursive(nSteps:int):
    if nSteps < 0:
        return 0
    elif nSteps == 0:
        return 1
    else:
        return countWaysRecursive(nSteps - 1) + countWaysRecursive(nSteps - 2) + countWaysRecursive(nSteps - 3)


# Memoization Pending
def countWaysMemo(nSteps:int):
    pass


# ways = TripleStepRecursive(3)
# ways = TripleStepIterative(2)
# print(ways)

print(countWaysRecursive(4))
