from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        row, column = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, column-1, 0, row-1
        result = []
        while left <= right and top <= bottom:
            for c in range(left, right+1):
                print(top, c)
                result.append(matrix[top][c])

            for r in range(top+1, bottom+1):
                print(r, right)
                result.append(matrix[r][right])

            if left < right and top < bottom:
                for c in range(right-1, left, -1):
                    print(bottom, c)
                    result.append(matrix[bottom][c])

                for r in range(bottom, top, -1):
                    print(r, left)
                    result.append(matrix[r][left])

            left, right, top, bottom = left+1, right-1, top+1, bottom-1

        return result


s = Solution()
m = [[3, 2]]
r = s.spiralOrder(m)
print(r)
