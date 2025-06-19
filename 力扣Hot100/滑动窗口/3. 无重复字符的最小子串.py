# 示例 1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        max_sub_len = 1
        left_i, right_j = 0, 1
        char_stat = {s[0]: 1}

        while right_j < len(s):
            ch = s[right_j]
            if char_stat.get(ch, 0) == 0:
                char_stat[ch] = 1
                max_sub_len = max(max_sub_len, right_j - left_i + 1)
                right_j += 1
            else:
                char_stat[s[left_i]] -= 1
                left_i += 1

        return max_sub_len

