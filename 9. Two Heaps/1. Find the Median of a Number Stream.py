import heapq

class MedianOfAStream:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def insert_num(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

        return -self.maxHeap[0] / 1.0

def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print(str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print(str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print(str(medianOfAStream.find_median()))

main()