# 时间复杂度 O(mn)
# 空间复杂度 O(mn)
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 广度优先遍历
        rows, cols = len(grid), len(grid[0])
        dq = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    dq.append((i, j, 0))
                    grid[i][j] = 0

        max_time = 0
        next_change = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while dq:
            i, j, time = dq.popleft()  # 左边pop
            for n in next_change:
                n_i = i + n[0]
                n_j = j + n[1]
                if 0 <= n_i <= rows - 1 and 0 <= n_j <= cols - 1 and grid[n_i][n_j] == 1:
                    grid[n_i][n_j] = 0
                    dq.append((n_i, n_j, time + 1))
                    max_time = max(max_time, time + 1)

        for i in range(rows):
            if sum(grid[i]) > 0:
                return -1

        return max_time


print(Solution().orangesRotting([[2, 1, 1], [1, 1, 1], [0, 1, 2]]))
