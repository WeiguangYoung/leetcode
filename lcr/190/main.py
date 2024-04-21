class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        x = 0xffffffff
        dataA, dataB = dataA & x, dataB & x
        while dataB != 0:
            dataA, dataB = (dataA ^ dataB), (dataA & dataB) << 1 & x
        return dataA if dataA <= 0x7fffffff else ~(dataA ^ x)


s = Solution()
s.encryptionCalculate(5, -1)
