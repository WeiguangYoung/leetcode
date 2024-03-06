def backtrack(
    state: list,
    target: int,
    start: int,
    choices: list,
    res: list,
):
    """回溯算法：子集和 I"""
    if target == 0:
        res.append(state)
        return

    for i in range(start, len(choices)):
        if target - choices[i] < 0:
            break

        if i > start and choices[i] == choices[i-1]:
            continue

        state.append(choices[i])

        backtrack(state, target-choices[i], i+1, choices, res)

        state.pop()


def subset_sum_i_naive(nums: list, target: int) -> list:
    """求解子集和 I（包含重复子集）"""
    state = []
    res = []
    nums.sort()
    backtrack(state, target, 0, nums, res)

    return res
