import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = collections.deque()
        dire = collections.deque()

        for i, ch in enumerate(senate):
            if ch == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while dire and radiant:
            if dire[0] < radiant[0]:
                dire.append(dire[0]+n)
            else:
                radiant.append(radiant[0]+n)

            dire.popleft()
            radiant.popleft()

        return "Dire" if dire else "Radiant"


s = Solution()
s.predictPartyVictory("DDRRR")
