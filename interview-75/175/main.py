from typing import List


class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        counts = [0]*32
        for action in actions:
            for i in range(32):
                counts[i] += action & 1
                action >>= 1
        
        res = 0
        for i in range(32):
            res <<= 1
            res |= counts[i]%3
        
        return res

