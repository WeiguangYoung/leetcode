from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt0 = 0
        ans = 0
        left = 0
        for right in range(len(nums)):
            cnt0 += 1-nums[right]
            while cnt0>k:
                cnt0 -= 1-nums[left]
                left += 1
            ans = max(ans, right-left+1)
        return ans