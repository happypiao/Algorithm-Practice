from collections import deque


class Solution:
    TAG_MAP = {
        "[": "]",
        "(": ")",
        "{": "}"
    }
    def isValid(self, s: str) -> bool:
        dq = deque()

        for c in s:
            if c in "([{":
                dq.append(c)
            else:
                if (not dq) or self.TAG_MAP.get(dq.pop(), None) != c:
                    return False

        return len(dq) == 0
