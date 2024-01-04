class Solution:
    def replaceSpace(self, s: str) -> str:
        # return s.replace(" ", "%20")
        # return '%20'.join(s.split(' '))
        return ''.join(('%20' if c==' ' else c for c in s))
