from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        results = [[chars[0], 1]]
        for i in range(1, len(chars)):
            if results[-1][0] == chars[i]:
                results[-1][1] += 1
            else:
                results.append([chars[i], 1])

        i = 0
        for item in results:
            chars[i] = item[0]
            i += 1
            if item[1] != 1:
                tmp = len(str(item[1]))
                chars[i:i+tmp] = str(item[1])
                i += tmp

        chars = chars[:i]
        return len(chars)


class Solution:
    # TODO review

    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = left = 0
        for read in range(n):
            if read == n-1 or chars[read] != chars[read+1]:
                chars[write] = chars[read]
                write += 1
                num = read - left + 1
                if num > 1:
                    l = len(str(num))
                    chars[write:write+l] = str(num)
                    write += l
                left = read + 1

        return write


s = Solution()
s.compress(["a", "a", "b", "b", "c", "c", "c"])
