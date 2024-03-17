from typing import List


class Solution:
    def crackPassword(self, password: List[int]) -> str:
        def quick_sort(l, r):
            if l >= r:
                return
            i, j = l, r
            while i < j:
                # 从最后一个向前比较，比较对象为l
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j:
                    j -= 1
                # 从第一个向前比较，比较对象为l
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                    i += 1

                # 交换i和j的位置
                strs[i], strs[j] = strs[j], strs[i]

            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        strs = [str(num) for num in password]
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)


s = Solution()
result = s.crackPassword([6, 5, 4, 3, 2, 1])
print(result)
