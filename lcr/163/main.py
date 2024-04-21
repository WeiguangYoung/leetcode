class Solution:
    def findKthNumber(self, k: int) -> int:
        digit, start, count = 1, 1, 9
        while k > count:  # 1.
            k -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (k - 1) // digit  # 2.
        return int(str(num)[(k - 1) % digit])  # 3.
