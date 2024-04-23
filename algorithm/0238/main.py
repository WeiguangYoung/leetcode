from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        results = [1]
        for i in range(1, len(nums)):
            results.append(results[i-1]*nums[i-1])

        tmp = 1
        for i in range(len(nums)-2, -1, -1):
            tmp *= nums[i+1]
            results[i] *= tmp

        return results


s = Solution()
s.productExceptSelf([-1, 1, 0, -3, 3])
