from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def search(nums, k):
            if not nums:
                return 0
            pivot = nums[0]
            small, equal, big = [], [], []
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if len(small) > len(nums)-k:
                return search(small, k-len(big)-len(equal))
            if len(big) >= k:
                return search(big, k)

            return pivot

        return search(nums, k)
