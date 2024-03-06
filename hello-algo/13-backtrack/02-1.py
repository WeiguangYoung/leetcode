def backtrack(
    state: list, choices: list, selected: list, res: list
):
    """回溯算法：全排列 I"""
    # 当状态长度等于元素数量时，记录解
    if len(state) == len(choices):
        res.append(list(state))
        return

    # 遍历所有选择
    for i, choice in enumerate(choices):
        if not selected[i]:
            selected[i] = True
            state.append(choice)
            backtrack(state, choices, selected, res)
            selected[i] = False
            state.pop()


def permutations_i(nums: list) -> list:
    """全排列 I"""
    res = []
    backtrack(state=[], choices=nums, selected=[False] * len(nums), res=res)
    return res


print(permutations_i([1, 2, 3]))
