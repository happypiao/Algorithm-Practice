from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 1. 统计每个字母最远下标
        char_index = [0] * 26
        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            char_index[index] = max(char_index[index], i)
        # 2. 遍历
        left = 0
        cur_index = 0
        i = 0
        result = []
        while i <= len(s) - 1:
            c_index = ord(s[i]) - ord('a')
            cur_index = max(cur_index, char_index[c_index])
            if i == cur_index:
                result.append(i - left + 1)
                if i == len(s) - 1:
                    break
                left = i + 1

            i += 1

        return result

# print(Solution().partitionLabels("eccbbbbdec"))