class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        m, n = len(frame), len(frame[0])
        for j in range(1, n): # 初始化第一行
            frame[0][j] += frame[0][j - 1]
        for i in range(1, m): # 初始化第一列
            frame[i][0] += frame[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                frame[i][j] += max(frame[i][j - 1], frame[i - 1][j])
        return frame[-1][-1]