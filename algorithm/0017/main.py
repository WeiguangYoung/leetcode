from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        if not digits:
            return results

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(index):
            if len(digits) == index:
                results.append("".join(result))
                return

            for c in phone_map.get(digits[index], ""):
                result.append(c)
                backtrack(index+1)
                result.pop()

        result = []
        backtrack(0)
        return results
