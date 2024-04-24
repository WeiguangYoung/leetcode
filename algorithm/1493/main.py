from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums)-1

        cnt0 = 0
        left = 0
        ans = 0
        for right, num in enumerate(nums):
            cnt0 += 1-num
            while cnt0 > 1:
                cnt0 -= 1 - nums[left]
                left += 1

            ans = max(ans, right-left+1)
        return ans - 1
