from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        定义子问题
        初始值 dp[0] = 0  dp[1] = 1
        递推关系 dp[i] = max(dp[i-1], dp[i-2]+cost[i-1])
        dp定义 dp[i]
        状态转移
        """
        dp = [0]*(len(nums)+1)
        dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])

        return dp[-1]
