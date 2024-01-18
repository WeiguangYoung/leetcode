from typing import List


class Solution:
    def goodsOrder(self, goods: str) -> List[str]:
        values, results = list(goods), []

        def dfs(x):
            if x == len(values)-1:
                print
                results.append("".join(values))
                return

            s = set()
            for i in range(x, len(values)):
                if values[i] in s:
                    continue
                s.add(values[i])
                values[i], values[x] = values[x], values[i]
                dfs(x+1)
                values[x], values[i] = values[i], values[x]

        dfs(0)

        return results
