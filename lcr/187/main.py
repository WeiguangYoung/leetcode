class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        x = 0
        for i in range(2, num + 1):
            x = (x + target) % i
        return x
