from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        exist_to_0 = []
        for conn in connections:
            if conn[1] == 0:
                exist_to_0.append(conn[0])
        
        
