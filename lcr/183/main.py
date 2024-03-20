from typing import List
import collections


class Solution:
    def maxAltitude(self, heights: List[int], limit: int) -> List[int]:
        if not heights or limit == 0:
            return []

        deque = collections.deque()
        for i in range(limit):
            while deque and heights[i] > deque[-1]:
                deque.pop()
            deque.append(heights[i])

        results = [deque[0]]
        for i in range(limit, len(heights)):
            if heights[i-limit] == deque[0]:
                deque.popleft()

            while deque and heights[i] > deque[-1]:
                deque.pop()
            
            deque.append(heights[i])
            results.append(deque[0])
        
        return results