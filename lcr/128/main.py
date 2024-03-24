from typing import List


class Solution:
    def stockManagement(self, stock: List[int]) -> int:
        i, j = 0, len(stock) - 1
        while i < j:
            m = (i + j) // 2
            if stock[m] > stock[j]:
                i = m+1
            elif stock[m] < stock[j]:
                j = m
            else:
                return min(stock[i:j])
        return stock[i]


s = Solution()
index = s.stockManagement(stock=[5, 7, 9, 1, 2])
print(index)
