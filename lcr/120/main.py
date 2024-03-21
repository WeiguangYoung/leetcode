from typing import List


class Solution:
    def findRepeatDocument(self, documents: List[int]) -> int:
        i = 0
        while i < len(documents):
            if documents[i] == i:
                i += 1
                continue

            if documents[documents[i]] == documents[i]:
                return documents[i]
            
            documents[documents[i]
                      ], documents[i] = documents[i], documents[documents[i]]
        return -1
