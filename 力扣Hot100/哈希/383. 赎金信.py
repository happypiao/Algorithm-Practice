# https://leetcode.cn/problems/ransom-note/description/
# 代码随想录 https://www.programmercarl.com/0383.%E8%B5%8E%E9%87%91%E4%BF%A1.html#%E6%80%9D%E8%B7%AF
# 时间复杂度 O(N+M)
# 空间复杂度 O(S)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_stat = [0] * 26

        for ch in magazine:
            char_stat[ord(ch) - ord('a')] += 1

        for rc in ransomNote:
            ch_index = ord(rc) - ord('a')
            char_stat[ch_index] -= 1
            if char_stat[ch_index] < 0:
                return False

        return True
