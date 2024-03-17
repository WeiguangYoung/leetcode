class Solution:
    def pathEncryption(self, path: str) -> str:
        res = []
        for c in path:
            if c == '.': res.append(' ')
            else: res.append(c)
        return "".join(res)

