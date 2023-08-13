class Solution:
    def strToInt(self, s: str) -> int:
        i = 0
        result = 0
        max_int, min_int = 2**31-1, -2**31

        for x in s:
            if x == " ":
                i += 1
            else:
                break

        if i > len(s)-1:
            return 0

        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            sign = 1
            i += 1
        else:
            sign = 1

        end = 2**31//10
        for n in s[i:]:
            if n > '9' or n < '0':
                break

            if result > end or result == end and n > '7':
                return max_int if sign == 1 else min_int

            result = result * 10+ord(n)-ord("0")

        return result*sign


s = Solution()
r = s.strToInt("-2147483647")
print(r)
