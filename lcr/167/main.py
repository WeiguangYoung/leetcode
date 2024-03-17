class Solution:
    def dismantlingAction(self, arr: str) -> int:
        map = {}
        res = 0
        i = -1
        for j in range(arr):
            if arr[j] in map:
                i = max(map[arr[j]], i)

            map[arr[j]] = j
            res = max(res, j-i)
        return res
