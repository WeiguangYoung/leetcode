from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        初始值 dp[0] = 0 dp[1] = 0
        状态转移：dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]  )
        """
        dp = [0] * (len(cost)+1)

        for i in range(2, len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        
        return dp[-1]