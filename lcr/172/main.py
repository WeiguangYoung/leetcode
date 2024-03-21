from typing import List


class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:

        def get_target_index(t):
            l, r = 0, len(scores)-1
            while l <= r:
                mid = (l+r)//2
                if scores[mid] > t:
                    r -= 1
                else:
                    l += 1
            return l

        return get_target_index(target) - get_target_index(target-1)
