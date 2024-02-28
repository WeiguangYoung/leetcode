def bucket_sort(nums: list):
    """桶排序"""
    # 初始化 k = n/2 个桶，预期向每个桶分配 2 个元素
    k = len(nums) // 2
    buckets = [[] for _ in range(k)]

    # 1. 将数组元素分配到各个桶中
    for num in nums:
        i = int(num*k)
        buckets[i].append(num)

    i = 0
    for bucket in buckets:
        bucket.sort()
        for num in bucket:
            nums[i] = num
            i += 1



bucket_sort([0.5, 0.25, 0.6, 0.4, 0.75, 0.3, 0.8])
