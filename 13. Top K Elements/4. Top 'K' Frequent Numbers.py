from heapq import *

nums = [5, 12, 11, 3, 11]
k = 2

num_dict = {}

for num in nums:
    if num not in num_dict:
        num_dict[num] = 0
    num_dict[num] += 1

heap = []
for num, freq in list(num_dict.items())[:k]:
    heappush(heap, (freq, num))

for num, freq in list(num_dict.items())[k:]:
    if freq > heap[0][0]:
        heappop(heap)
        heappush(heap, (freq, num))

print([num for freq, num in list(heap)])
