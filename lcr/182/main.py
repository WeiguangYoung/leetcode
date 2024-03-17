class Solution:
    def dynamicPassword(self, password: str, target: int) -> str:
        res = []
        for i in range(target, len(password)):
            res.append(password[i])
        for i in range(target):
            res.append(password[i])
        return ''.join(res)
