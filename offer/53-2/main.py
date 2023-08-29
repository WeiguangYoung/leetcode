from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if len(nums) == 1:
            if nums[0] == 1:
                return 0
            else:
                return 1

        while left < right:
            mid = (left+right) // 2
            if nums[mid] == mid:
                left = mid+1
            else:
                right = mid-1

        return left


s = Solution()
r = s.missingNumber([0])
print(r)
