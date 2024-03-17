'''
Author: yangweiguang yangweiguang@uniml.com
Date: 2023-05-05 13:50:51
LastEditors: yangweiguang yangweiguang@uniml.com
LastEditTime: 2023-05-05 14:37:44
FilePath: /leetcode/1031/main2.py
Description: 

Copyright (c) 2023 by GuangjiTech, All Rights Reserved. 
'''

"""
我们先预处理得到数组nums的前缀和数组s其中si表示nums中前个元素的和。

接下来，我们分两种情况枚举
假设 firstLen个元素的子数组在
secondLen个元素的子数组的左边，那么我们可以枚举 secondLen 个元素的子数组的左端点i，用变量 t 维护左边 firstLen 个元素的子数组的最大和，那么当前最大和就是t+sli+secondLen-sli 。其中
sli+secondLen-si 表示 secondLen 个元素的子数组的和。枚举完所有的i，就得到了第一种情况下的最大和。
假设 secondLen个元素的子数组在
firstLen个元素的子数组的左边，那么我们可以枚举firstLen个元素的子数组的左端点i，用变量t维护左边 secondLen 个元素的子数组的最大和，那么当前最大和就是
t+sli+firstLen-sli 。其中
si+firstLen-si 表示 firstLen 个元素的子数组的和。枚举完所有的i，就得到了第二种情况下的最大和。
取两种情况下的最大值作为答案即可
"""


class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        maxSum = 0
        l = len(nums)
        s = []

        for i in range(1, l+1):
            s.append
            nums[i] += nums[i-1]

        t = 0
        for i in range(firstLen, l-secondLen+1):
            t = max(t, nums[i]-nums[i-firstLen])
            maxSum = max(maxSum, t+nums[i+secondLen]-nums[i])
        print(maxSum)

        return maxSum


s = Solution()

result = s.maxSumTwoNoOverlap([12, 8, 12, 18, 19, 10, 17, 20,
                               6, 8, 13, 1, 19, 11, 5], 3, 6)
print(result)
