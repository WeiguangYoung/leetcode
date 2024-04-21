class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        v = 0
        z = 0
        for n in nums:
            if v == 0:
                z = n
            v += 1 if z == n else -1

        return z
