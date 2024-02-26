def selection_sort(nums: list):
    """选择排序"""
    n = len(nums)
    # 外循环：未排序区间为 [i, n-1]
    for i in range(n-1):
        k = i
        for j in range(i+1, n):
            if nums[j] < nums[k]:
                k = j
            nums[i], nums[k] = nums[k], nums[i]
