# 时间复杂度 O(N)
# 空间复杂度 O(N)
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        result = []
        length = len(p)
        cnt1 = Counter(p)
        cnt2 = Counter(s[:length - 1])

        for i in range(length - 1, len(s)):
            cnt2[s[i]] += 1
            if cnt2 == cnt1:
                result.append(i - length + 1)
            cnt2[s[i - length + 1]] -= 1

        return result
