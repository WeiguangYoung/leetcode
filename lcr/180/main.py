from typing import List


class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))

            if s >= target:
                i += 1
                s -= i
            else:
                j += 1
                s += j

        return res