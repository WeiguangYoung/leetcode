from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        i, j = 0, len(height)-1
        while i < j:
            if height[i] < height[j]:
                ans = max(ans, height[i]*(j-i))
                i += 1
            else:
                ans = max(ans, height[i]*(j-i))
                j -= 1

        return ans
