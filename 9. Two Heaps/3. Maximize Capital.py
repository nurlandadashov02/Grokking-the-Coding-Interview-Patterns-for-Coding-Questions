from heapq import *


def findMaximumCapital(capital, profits, numberOfProjects, initialCapital):
    minCapitalHeap = [(i , c) for c, i in enumerate(capital)]
    heapify(minCapitalHeap)
    maxProfitHeap = []

    availableCapital = initialCapital
    for _ in range(numberOfProjects):
        while len(minCapitalHeap) > 0 and minCapitalHeap[0][0] <= availableCapital:
            capital, index = heappop(minCapitalHeap)
            heappush(maxProfitHeap, (-profits[index], index))

        if not maxProfitHeap:
            break

        availableCapital -= maxProfitHeap[0][0]
        heappop(maxProfitHeap)

    return availableCapital


# print(findMaximumCapital([0, 1, 2], [1, 2, 3], 2, 1))
# print(findMaximumCapital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0))
# print(findMaximumCapital([0, 1, 1], [1, 2, 3], 2, 0))
print(findMaximumCapital([0, 1, 2], [1, 2, 3], 10, 0))
