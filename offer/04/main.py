from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        i, j = 0, len(matrix[0]) - 1

        while j >= 0 and i <= len(matrix) - 1:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True

        return False
