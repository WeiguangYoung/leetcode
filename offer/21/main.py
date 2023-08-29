from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        pa, pb = 0, len(nums)-1

        while (pa < pb):
            if nums[pa] % 2 == 1:
                pa += 1
            elif nums[pb] % 2 == 0:
                pb -= 1
            elif nums[pa] % 2 == 0 and nums[pb] % 2 == 1:
                nums[pa], nums[pb] = nums[pb], nums[pa]
                pa += 1
                pb -= 1
        
        return nums
