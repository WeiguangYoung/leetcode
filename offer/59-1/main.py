from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        queue = []
        # 找到第一个最大值
        for i in range(k):
            if i == 0:
                queue.append(nums[i])
            elif nums[i] >= queue[-1]:
                queue.append(nums[i])
        results.append(queue[-1])
        print(queue,results)

        for i in range(k, len(nums)):
            if nums[i] == nums[i-k]:
                queue = queue[1:]

            if (not queue) or nums[i] >= queue[-1]:
                queue.append(nums[i])

            results.append(queue[-1])
        return results
# 1 3 1 2 0 5    
# 3,1   3
# 3,1     
# 1    3

s= Solution()
result = s.maxSlidingWindow([1,3,1,2,0,5],3)
print(result)