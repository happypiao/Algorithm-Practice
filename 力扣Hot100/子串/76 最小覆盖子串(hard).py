from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_left, min_right = 0, len(s) - 1
        min_len = len(s) + 1
        cnt_s = Counter()
        cnt_t = Counter(t)

        left = 0
        find = False
        for right, c in enumerate(s):
            cnt_s[c] += 1

            while cnt_s >= cnt_t:
                if right - left + 1 < min_len:
                    min_left, min_right = left, right
                    min_len = right - left + 1
                    find = True
                cnt_s[s[left]] -= 1
                left += 1

        return s[min_left: min_right + 1] if find else ""
