from typing import List, Dict


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c, idx):
            if idx >= len(word):
                return True
            if board[r][c] != word[idx]:
                return False
            if visited[r][c]:
                return False

            visited[r][c] = True
            if r > 0 and dfs(r - 1, c, idx + 1):
                return True
            if r < m - 1 and dfs(r + 1, c, idx + 1):
                return True
            if c > 0 and dfs(r, c - 1, idx + 1):
                return True
            if c < n - 1 and dfs(r, c + 1, idx + 1):
                return True
            visited[r][c] = False

        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if (not visited[i][j]) and board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    if dfs(i, j, 0):
                        return True

        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    s = Solution()
    result = s.exist([["a"]], "a")
    print(result)
