from typing import List


class Solution:
    def checkDynasty(self, places: List[int]) -> bool:
        s = []
        for p in places:
            if p != 0:
                if p in s:
                    return False
                s.append(p)

        min_p, max_p = min(s), max(s)
        return max_p - min_p < 5
