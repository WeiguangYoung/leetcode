from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid

        return l

    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        nums.append(float("-inf"))
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid-1

        return l


s = Solution()
r = s.findPeakElement([1, 2, 3, 1])
print(r)
