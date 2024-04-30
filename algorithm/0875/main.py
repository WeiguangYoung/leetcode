from typing import List
from math import ceil


class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def up(m):
            s = 0
            for pile in piles:
                s += ceil(pile/m)
            return s <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left+right)//2
            if up(mid):
                right = mid
            else:
                left = mid+1

        return left


s = Solution()
s.minEatingSpeed([3, 6, 7, 11], 8)
