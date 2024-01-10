import random
from typing import List


class Solution:
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        stock.sort()
        return stock[:cnt]


class Solution2:
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, stock, l, r, cnt):
        pos = self.randomized_partition(stock, l, r)
        num = pos - l + 1
        if cnt < num:
            self.randomized_selected(stock, l, pos - 1, cnt)
        elif cnt > num:
            self.randomized_selected(stock, pos + 1, r, cnt - num)

    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        if cnt == 0:
            return list()
        self.randomized_selected(stock, 0, len(stock) - 1, cnt)
        return stock[:cnt]
