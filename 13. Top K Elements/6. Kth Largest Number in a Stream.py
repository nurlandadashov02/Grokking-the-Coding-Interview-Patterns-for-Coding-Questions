from heapq import *


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.heap = []
        for num in nums[:k]:
            heappush(self.heap, num)

        for num in nums[k:]:
            if num > self.heap[0]:
                heappop(self.heap)
                heappush(self.heap, num)

    def add(self, val: int) -> int:

        if len(self.heap) < self.k:
            heappush(self.heap, val)
            return self.heap[0]

        if val > self.heap[0]:
            heappop(self.heap)
            heappush(self.heap, val)

        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)