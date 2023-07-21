from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def search_index(tar):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left+right)//2
                if nums[mid] > tar:
                    right = mid-1
                else:
                    left = mid+1

            return left

        return search_index(target)-search_index(target-1)
