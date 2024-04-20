class Solution:
    def maxSales(self, sales: List[int]) -> int:
        for i in range(1, len(sales)):
            sales[i] += max(sales[i - 1], 0)
        return max(sales)