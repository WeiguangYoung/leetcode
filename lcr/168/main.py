import heapq


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
        return res[-1]


class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        factors = [2, 3, 5]
        seen = {1}
        heap = [1]

        for i in range(n - 1):
            curr = heapq.heappop(heap)
            for factor in factors:
                if (nxt := curr * factor) not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)

        return heapq.heappop(heap)


s = Solution2()
r = s.nthUglyNumber(10)
print(r)
