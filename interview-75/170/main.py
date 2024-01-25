from typing import List


class Solution:
    def reversePairs(self, record: List[int]) -> int:
        def merge_sort(left, right):
            print(left, right)
            if left >= right:
                return 0

            mid = (left+right)//2
            result = merge_sort(left, mid) + merge_sort(mid+1, right)

            tmp = [0] * (right-left+1)
            i, j, k = left, mid+1, 0
            while i <= mid and j <= right:
                if record[i] > record[j]:
                    tmp[k] = record[j]
                    result += mid - i + 1
                    j += 1
                else:
                    tmp[k] = record[i]
                    i += 1
                k += 1

            while i <= mid:
                tmp[k] = record[i]
                i += 1
                k += 1

            while j <= right:
                tmp[k] = record[j]
                j += 1
                k += 1

            for k in range(len(tmp)):
                record[left+k] = tmp[k]

            return result

        return merge_sort(0, len(record)-1)


s = Solution()
r = s.reversePairs([7, 5, 6, 4])
print(r)
