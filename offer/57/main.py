from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pa, pb = 0, len(nums)-1
        while pa < pb:
            s = nums[pa]+nums[pb]
            if s == target:
                return [nums[pa], nums[pb]]
            elif s > target:
                pb -= 1
            else:
                pa += 1

        return []
