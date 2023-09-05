
class Solution:
    def __init__(self):
        self.ans = 0
    
    def sumNums(self, n: int) -> int:
        if n <= 0:
            return 0
        else:
            self.sumNums(n-1)
        
        self.ans += n
        return self.ans
    

s = Solution()
s.sumNums(3)