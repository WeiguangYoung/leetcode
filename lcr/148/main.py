from typing import List


class Solution:
    def validateBookSequences(self, putIn: List[int], takeOut: List[int]) -> bool:
        i = 0
        stack = []

        for num in putIn:
            stack.append(num)

            while stack and stack[-1] == takeOut[i]:
                stack.pop()
                i += 1

        return not stack
