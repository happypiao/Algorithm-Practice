# 时间复杂度 O(mn)
# 空间复杂度 O(mn)
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        next_visit = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def deep_search(grid, i, j, count):
            if i < 0 or i > rows - 1 or j < 0 or j > cols - 1 or visited[i][j] == 1 or grid[i][j] == 0:
                return count
            visited[i][j] = 1
            count += 1
            for n in next_visit:
                n_i = i + n[0]
                n_j = j + n[1]
                count = deep_search(grid, n_i, n_j, count)

            return count

        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    result = max(result, deep_search(grid, i, j, 0))

        return result
