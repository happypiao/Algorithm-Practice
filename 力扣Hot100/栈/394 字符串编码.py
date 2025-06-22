# 时间复杂度 O(N)
# 空间复杂度 O(N)

class Solution:
    def decodeString(self, s: str) -> str:
        tmp_stack = []
        res = ""
        repeat_n = 0

        for c in s:
            if c.isdigit():
                repeat_n = repeat_n * 10 + int(c)
            elif c == "[":
                tmp_stack.append((res, repeat_n))
                res, repeat_n = "", 0
            elif c == "]":
                last_s, rep_n = tmp_stack.pop()
                res = last_s + repeat_n * res
            else:
                res += c

        return res