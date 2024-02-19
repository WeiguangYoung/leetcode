import heapq
from typing import List


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []    # 4 5 6
        self.max_heap = []    # -3 -2 -1

    def addNum(self, num: int) -> None:
        # 长度相等时，min_heap进一出一，max_heap进一
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        # 长度不等时，max_heap进一出一，min_heap进一  (len(max_heap) >= len(max_heap))
        else:
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        return (self.min_heap[0]-self.max_heap[0])/2 if len(self.min_heap) == len(self.max_heap) else -self.max_heap[0]


s = MedianFinder()

s.addNum(4)
s.addNum(2)
s.addNum(5)
s.addNum(1)
s.addNum(6)
s.addNum(3)
s.addNum(7)

r = s.findMedian()
print(r)
