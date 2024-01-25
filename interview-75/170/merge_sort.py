from typing import List


def merge(nums: List[int], left: int, mid: int, right: int):
    tmp = [0]*(right - left + 1)
    i, j, k = left, mid + 1, 0
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1

    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1

    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1

    for k in range(len(tmp)):
        nums[left+k] = tmp[k]


def merge_sort(nums: List[int], left: int, right: int):
    # 终止条件，子数组长度=1
    if left >= right:
        return

    # 计算中点
    mid = (left+right)//2

    # 递归左右子数组
    merge_sort(nums, left, mid)
    merge_sort(nums, mid+1, right)

    # 合并
    merge(nums, left, mid, right)
