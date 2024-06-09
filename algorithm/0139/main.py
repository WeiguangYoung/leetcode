from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[n]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def backtrack(s):
            if not s:
                return True
            
            res = False
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    res = backtrack(s[i:]) or res

            return res

        return backtrack(s)


s = Solution()
s.wordBreak("leetcode", ["leet", "code"])
