class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        targets = "aeiou"
        s2 = [int(c in targets) for c in s]
        max_total = sum(s2[:k])
        cur_total = max_total
        
        for i in range(k, len(s2)):
            cur_total += (s2[i]-s2[i-k])
            max_total = max(max_total, cur_total)

        return max_total


s = Solution()
print(s.maxVowels("ccaaae", 4))
