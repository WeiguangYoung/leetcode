from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        results = []

        for i in range(k):
            if i == 0:
                queue.append(nums[i])
            elif nums[i] >= queue[-1]:
                queue.append(nums[i])

        results.append(queue[-1])

        for i in range(k, len(nums)):
            if nums[i] < nums[i - k]:
                pass
            elif nums[i] == nums[i - k]:
                pass
            else:
                pass

            if nums[i] == queue[0]:
                queue = queue[1:]
            elif nums[i] >= queue[-1]:
                queue.append(nums[i])

            results.append(queue[-1])

        return results


s = Solution()
r = s.maxSlidingWindow([1, 3, -1, 4, 5, 3, 6, 7], 3)
print(r)
