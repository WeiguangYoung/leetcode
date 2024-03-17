from typing import List


class Solution:
    def goodsOrder(self, goods: str) -> List[str]:
        values, results = list(goods), []
        values.sort()

        l = len(values)
        perm = []
        vis = [False for _ in range(l)]

        def dfs(x):
            if x == l:
                results.append("".join(perm))
                return

            for i in range(l):
                if vis[i] or (i > 0 and values[i] == values[i-1] and not vis[i-1]):
                    continue

                vis[i] = True
                perm.append(values[i])
                dfs(x+1)
                perm.pop()
                vis[i] = False

        dfs(0)
        return results


s = Solution()
results = s.goodsOrder("cab")
print(results)
