from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        def ok(spell):
            i, j = 0, len(potions)-1
            while i <= j:
                mid = (i+j)//2
                if potions[mid] * spell >= success:
                    j = mid-1
                else:
                    i = mid+1

            return len(potions)-i

        return [ok(spell) for spell in spells]


s = Solution()
s.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7)
