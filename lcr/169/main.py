class Solution:
    def dismantlingAction(self, arr: str) -> str:
        hmap = {}
        for c in arr:
            hmap[c] = not c in hmap
        for k, v in hmap.items():
            if v:
                return k
        return ' '
