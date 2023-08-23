from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers) == 1:
            return numbers[0]

        i, j = 0, len(numbers) - 1

        while i <= j:
            mid = (i + j) // 2
            if numbers[mid] < numbers[j]:
                j = mid
            elif numbers[mid] > numbers[j]:
                i = mid + 1
            else:
                j -= 1

        return numbers[i]


s = Solution()
r = s.minArray(numbers=[3, 4, 5, 1, 2])
print(r)
