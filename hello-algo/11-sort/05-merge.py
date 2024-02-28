def merge(nums: list, left: int, mid: int, right: int):
    tmp = [0]*(right-left+1)
    i, j, k = left, mid+1, 0
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

    

def merge_sort(nums: list, left: int, right: int):
    """归并排序"""
    if left >= right:
        return

    mid = (left+right)//2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid+1, right)

    merge(nums, left, mid, right)
    print(nums)



merge_sort([4, 2, 8, 3, 7, 6, 5, 1], 0, 7)
