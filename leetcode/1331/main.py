class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {j: i for i, j in enumerate(sorted(set(arr)), 1)}
        return [ranks[i] for i in arr]
