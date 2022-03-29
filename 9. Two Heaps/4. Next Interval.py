from heapq import *

intervals = [[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]

maxEndHeap = []
maxStartHeap = []

for index, interval in enumerate(intervals):
    heappush(maxEndHeap, (-interval[1], index))
    heappush(maxStartHeap, (-interval[0], index))

heapify(maxEndHeap)
heapify(maxStartHeap)

res = [-1] * len(intervals)

while maxEndHeap:
    end, endIndex = heappop(maxEndHeap)
    if -maxStartHeap[0][0] >= -end:
        while maxStartHeap and -maxStartHeap[0][0] >= -end:
            start, startIndex = heappop(maxStartHeap)

        res[endIndex] = startIndex
        heappush(maxStartHeap, (start, startIndex))


print(res)
