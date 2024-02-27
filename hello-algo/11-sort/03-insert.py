def insertion_sort(nums: list):
    """插入排序"""
    # 外循环：已排序区间为 [0, i-1]
    for i in range(1, len(nums)):
        base = nums[i]

        j = i - 1

        while j >= 0 and nums[j] > base:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = base

    print(nums)


insertion_sort([4, 5, 3, 2, 6, 1])
