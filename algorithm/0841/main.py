from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = [0]
        visit = set()

        while queue:
            room_id = queue.pop(0)
            if room_id in visit:
                continue

            visit.add(room_id)
            for key in rooms[room_id]:
                queue.append(key)
        return len(visit) == len(rooms)


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(x: int):
            vis.add(x)
            nonlocal num
            num += 1

            for key in rooms[x]:
                if key not in vis:
                    dfs(key)

        n = len(rooms)
        num = 0
        vis = set()
        dfs(0)
        return num == n


s = Solution()
s.canVisitAllRooms([[1], [2], [3], []])
