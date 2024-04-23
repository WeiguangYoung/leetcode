from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False

        left_min = [0]*len(nums)
        left_min[0] = nums[0]
        for i in range(1, len(nums)):
            left_min[i] = min(left_min[i-1], nums[i])

        right_max = [0]*len(nums)
        right_max[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])

        for i in range(1, len(nums)-1):
            if left_min[i-1] < nums[i] < right_max[i+1]:
                return True
        return False


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return False

        first, second = nums[0], float("inf")
        for i in range(1, len(nums)):
            num = nums[i]
            if num > second:
                return True
            elif num > first:
                second = num
            else:
                first = num
        return False


s = Solution()
s.increasingTriplet([20, 100, 10, 12, 5, 13])
