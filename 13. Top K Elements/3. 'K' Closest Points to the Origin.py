from heapq import *
import math

points = [[1,2],[1,3]]
k = 1

heap = []

for point in points[:k]:
    heappush(heap, (-math.sqrt(point[0] ** 2 + point[1] ** 2), point))

res = []
for point in points[k:]:
    dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
    if dist < -heap[0][0]:
        heappop(heap)
        heappush(heap, (-dist, point))


print([p[1] for p in heap])