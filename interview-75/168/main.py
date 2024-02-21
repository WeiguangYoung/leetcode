class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res, n2, n3, n5 = [1]*n, 0, 0, 0
        for i in range(1, n):
            n = min(res[n2]*2, res[n3]*3, res[n5]*5)
            res[i] = n
            if n == res[n2]*2:
                n2 += 1
            if n == res[n3]*3:
                n3 += 1
            if n == res[n5]*5:
                n5 += 1
            print(res)
        return res[-1]


s = Solution()
r = s.nthUglyNumber(10)
print(r)
