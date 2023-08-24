import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        position = dict()
        q = collections.deque()
        n = len(s)

        for i, ch in enumerate(s):
            if ch not in position:
                position[ch] = i
                q.append((ch, i))
            else:
                position[ch] = -1
                while q and position[q[0][0]] == -1:
                    q.popleft()

        return q[0][0] if q else " "
