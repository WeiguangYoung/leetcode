from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(num, target):
            if len(result) == k:
                if target == 0:
                    results.append(result[:])
                return

            if num == 10 or num > target:
                return

            # 尝试num
            result.append(num)
            backtrack(num+1, target-num)
            result.pop()

            # 向后尝试
            backtrack(num+1, target)

        result = []
        results = []
        backtrack(1, n)
        return results


s = Solution()
s.combinationSum3(3, 9)
