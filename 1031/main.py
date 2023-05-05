'''
Author: yangweiguang yangweiguang@uniml.com
Date: 2023-04-26 09:40:22
LastEditors: yangweiguang yangweiguang@uniml.com
LastEditTime: 2023-05-05 13:39:52
FilePath: /leetcode/1031/main.py
Description:

Copyright (c) 2023 by GuangjiTech, All Rights Reserved.
'''


class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        # maxNum = 0
        # for i in range(len(nums) - firstLen + 1):
        #     for j in range(len(nums) - secondLen + 1):
        #         if j+secondLen <= i or j >= i+firstLen:
        #             curNum = sum(nums[i:i+firstLen])+sum(nums[j:j+secondLen])
        #             if maxNum < curNum:
        #                 maxNum = curNum
        
        maxNum = 0
        first = 0
        second = 0
        for i in range(len(nums) - firstLen+1):
            if secondLen <= i:
                first = sum(nums[i:i+firstLen])
                second = sum(nums[i-secondLen+1:i+1])
                thisNum = first + second
                print(
                    nums[i:i+firstLen],
                    nums[i-secondLen:i],
                )
                if maxNum <= thisNum:
                    maxNum = thisNum
        print("---------------------------------------------------------")
        for i in range(len(nums) - firstLen+1):
            if i <= len(nums)-secondLen-3:
                first = sum(nums[i:i+firstLen])
                second = sum(nums[i+firstLen-1:i+firstLen+secondLen-1])
                thisNum = first + second
                print(
                    nums[i:i+firstLen],
                    nums[i+firstLen:i+firstLen+secondLen],
                )
                if maxNum <= thisNum:
                    maxNum = thisNum

        return maxNum


s = Solution()

result = s.maxSumTwoNoOverlap([12, 8, 12, 18, 19, 10, 17, 20,
                               6, 8, 13, 1, 19, 11, 5], 3, 6)
print(result)
