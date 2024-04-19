def min_cost_climbing_stairs_dp(cost: list) -> int:
    """爬楼梯最小代价：动态规划"""
    n = len(cost) - 1
    if n == 1 or n == 2:
        return cost[n]

    dp = [-1]*(n+1)
    dp[1], dp[2] = cost[1], cost[2]
    for i in range(3, n+1):
        dp[i] = min(dp[i-1], dp[i-2])+cost[i]

    return dp[-1]


def min_cost_climbing_stairs_dp2(cost: list) -> int:
    """爬楼梯最小代价：动态规划"""
    n = len(cost) - 1
    if n == 1 or n == 2:
        return cost[n]

    a, b = cost[1], cost[2]
    for i in range(3, n+1):
        a, b = b, min(a, b)+cost[i]

    return b


def climbing_stairs_constraint_dp(n: int) -> int:
    """带约束爬楼梯：动态规划"""
    if n == 1 or n == 2:
        return 1

    dp = [[0]*3 for _ in range(n+1)]

    dp[1][1], dp[1][2] = 1, 0
    dp[2][1], dp[2][2] = 0, 1
    for i in range(3, n+1):
        dp[i][1] = dp[i-1][2]
        dp[i][2] = dp[i-2][1]+dp[i-2][2]

    return dp[-1][1] + dp[-1][2]


# print(min_cost_climbing_stairs_dp([0, 1, 10, 1]))

print(climbing_stairs_constraint_dp(6))
