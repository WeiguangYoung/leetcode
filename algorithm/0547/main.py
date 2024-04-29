from typing import List
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        n = len(isConnected)
        visited = set()
        results = 0
        for i in range(n):
            if i not in visited:
                queue = deque([i])
                while queue:
                    cur = queue.popleft()
                    visited.add(cur)
                    for j in range(len(isConnected[cur])):
                        if isConnected[cur][j] and j not in visited:
                            queue.append(j)

                results += 1

        return results


s = Solution()
s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
