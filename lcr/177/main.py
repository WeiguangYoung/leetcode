from typing import List

class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        x, y, n, m = 0, 0, 0, 1
        for num in sockets:      # 1. 遍历异或
            n ^= num
        while n & m == 0:        # 2. 循环左移，计算 m
            m <<= 1       
        for num in sockets:      # 3. 遍历 sockets 分组
            if num & m: x ^= num # 4. 当 num & m != 0
            else: y ^= num       # 4. 当 num & m == 0
        return x, y              # 5. 返回出现一次的数字


s = Solution()
s.sockCollocation([4, 5, 2, 4, 6, 6])