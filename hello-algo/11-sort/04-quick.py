def partition(nums: list, left: int, right: int) -> int:
    i, j = left, right
    while i < j:
        while i < j and nums[i] <= nums[right]:
            i += 1
        while i < j and nums[j] >= nums[right]:
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]

    nums[j], nums[right] = nums[right], nums[j]
    return j


def quick_sort(nums: list, left: int, right: int):
    if left >= right:
        return

    p = partition(nums, left, right)
    quick_sort(nums, left, p-1)
    quick_sort(nums, p+1, right)

    print(nums)


quick_sort([4, 5, 3, 2, 6, 1], 0, 5)
