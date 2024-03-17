from typing import List


class Solution:
    def statisticsProbability(self, num: int) -> List[float]:
        dp = [1/6]*6

        for n in range(1, num):
            tmp = [0]*(5*(n+1)+1)
            for i in range(len(dp)):
                for j in range(6):
                    print(i+j)
                    tmp[i+j] += dp[i]/6
            dp = tmp

        return dp


s = Solution()
s.statisticsProbability(3)
