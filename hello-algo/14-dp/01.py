import time


def dfs(i: int, mem: list) -> int:
    """搜索"""
    # 已知 dp[1] 和 dp[2] ，返回之
    if i == 1 or i == 2:
        return i

    if mem[i] != -1:
        return mem[i]

    count = dfs(i - 1, mem) + dfs(i - 2, mem)
    mem[i] = count

    return count


def climbing_stairs_dfs(n: int) -> int:
    """爬楼梯：搜索"""
    # mem = None
    mem = [-1] * (n+1)
    return dfs(n, mem)


def climbing_stairs_dp(n: int) -> int:
    """爬楼梯：搜索"""
    if n == 1 or n == 2:
        return n

    dp = [-1]*(n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n]


def climbing_stairs_dp2(n: int) -> int:
    """爬楼梯：搜索"""
    if n == 1 or n == 2:
        return n

    a, b = 1, 2
    for i in range(3, n+1):
        a, b = b, a+b

    return b


t1 = time.time()
# print(climbing_stairs_dfs(1000))
print(climbing_stairs_dp(1000))
t2 = time.time()
print(t2-t1)
