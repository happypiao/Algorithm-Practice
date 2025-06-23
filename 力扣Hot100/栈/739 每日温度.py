# 时间复杂度 O(N)
# 空间复杂度 O(N)
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 采用单调栈解决 单调递增
        n = len(temperatures)
        result = [0] * n
        stack = [(temperatures[0], 0)]

        for i in range(1, n):
            if temperatures[i] < stack[-1][0]:
                stack.append((temperatures[i], i))
            elif temperatures[i] == stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while stack and temperatures[i] > stack[-1][0]:
                    tmp, index = stack.pop()
                    result[index] = i - index

                stack.append((temperatures[i], i))

        return result
