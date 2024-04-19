"""
给定一个 m*n 的二维网格 grid ，网格中的每个单元格包含一个非负整数，表示该单元格的代价。
机器人以左上角单元格为起始点，每次只能向下或者向右移动一步，直至到达右下角单元格。
请返回从左上角到右下角的最小路径和。
"""


def min_path_sum_dfs(grid: list, i: int, j: int) -> int:
    """最小路径和：暴力搜索"""
    # 若为左上角单元格，则终止搜索
    if i == 0 and j == 0:
        return grid[0][0]
    # 若行列索引越界，则返回 +∞ 代价
    if i < 0 or j < 0:
        return "INF"
    # 计算从左上角到 (i-1, j) 和 (i, j-1) 的最小路径代价
    up = min_path_sum_dfs(grid, i - 1, j)
    left = min_path_sum_dfs(grid, i, j - 1)
    # 返回从左上角到 (i, j) 的最小路径代价
    return min(left, up) + grid[i][j]


def min_path_sum_dp(grid: list) -> int:
    m, n = len(grid), len(grid[0])

    dp = [[0]*m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for j in range(1, m):
        for i in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[n-1][m-1]


def min_path_sum_dp_comp(grid: list) -> int:
    """最小路径和：空间优化后的动态规划"""
    n, m = len(grid), len(grid[0])
    # 初始化 dp 表
    dp = [0] * m
    # 状态转移：首行
    dp[0] = grid[0][0]
    for j in range(1, m):
        dp[j] = dp[j - 1] + grid[0][j]
    # 状态转移：其余行
    for i in range(1, n):
        # 状态转移：首列
        dp[0] = dp[0] + grid[i][0]
        # 状态转移：其余列
        for j in range(1, m):
            dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
    return dp[m - 1]
