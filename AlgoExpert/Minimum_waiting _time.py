def minimumWaitingTime(queries):
    queries.sort()

    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        totalWaitingTime += duration * queriesLeft
    print(list(enumerate(queries)))
    return totalWaitingTime


queries = [3, 2, 1, 2, 6]
print(minimumWaitingTime(queries))
