def sift_down(nums: list, n: int, i: int):
    """堆的长度为 n ，从节点 i 开始，从顶至底堆化"""
    while True:
        l = 2*i+1
        r = 2*i+2
        ma = i

        if l < n and nums[l] > nums[ma]:
            ma = l

        if r < n and nums[r] > nums[ma]:
            ma = r

        if ma == i:
            break

        nums[i], nums[ma] = nums[ma], nums[i]
        i = ma


def heap_sort(nums: list):
    """堆排序"""
    for i in range(len(nums)//2, -1, -1):
        sift_down(nums, len(nums), i)

    for i in range(len(nums)-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(nums, i, 0)


heap_sort([4, 2, 8, 3, 7, 5, 1, 6])
