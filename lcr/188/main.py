from typing import List


class Solution:
    def bestTiming(self, prices: List[int]) -> int:
        cost, result = float("+inf"), 0
        for i in range(len(prices)):
            cost = min(cost, prices[i])
            result = max(result, prices[i]-cost)
        return result
