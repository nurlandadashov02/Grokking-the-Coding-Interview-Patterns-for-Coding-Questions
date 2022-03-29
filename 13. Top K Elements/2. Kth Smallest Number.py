from heapq import *

nums = [5, 12, 11, -1, 12]
k = 3

heap = []

for num in nums[:k]:
    heappush(heap, -num)

res = []
for num in nums[k:]:
    if num < -heap[0]:
        heappop(heap)
        heappush(heap, -num)


print(-heap[0])