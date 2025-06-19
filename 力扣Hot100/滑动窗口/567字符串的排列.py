# https://leetcode.cn/problems/permutation-in-string/description/
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。
# 换句话说，s1 的排列之一是 s2 的 子串 。
from collections import defaultdict, Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False

        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:n1 - 1])
        i = n1 - 1
        while i < n2:
            cnt2[s2[i]] += 1
            if cnt1 == cnt2:
                return True
            cnt2[s2[i-n1+1]] -= 1
            i += 1

        return False
