class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        pa = pb = len(s)-1

        results = []
        while pa >= 0:
            while pa >= 0 and s[pa] != " ":
                pa -= 1
            results.append(s[pa+1:pb+1])
            while s[pa] == " ":
                pa -= 1
            pb = pa
        return " ".join(results)


l = "the sky is blue"
s = Solution()
print(s.reverseWords(l))
