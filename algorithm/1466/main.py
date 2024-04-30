from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        metrics = [[0]*n for i in range(n)]
        for src, dst in connections:
            metrics[src][dst] = 1
        
        


s = Solution()
s.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
