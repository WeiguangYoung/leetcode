class Solution:
    def crackNumber(self, ciphertext: int) -> int:
        s = str(ciphertext)

        a, b = 1, 1
        for i in range(2, len(s)+1):
            tmp = s[i-2:i]
            a, b = (a+b, a) if "10" <= tmp <= "25" else (a, a)

        return a
