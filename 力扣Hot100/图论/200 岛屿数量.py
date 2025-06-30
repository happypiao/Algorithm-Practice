# 时间复杂度 O(mn)
# 空间复杂度 O(mn)
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        next_visit = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(grid, i, j):
            if grid[i][j] == "0":
                return
            visited[i][j] = 1
            for n in next_visit:
                n_i = i + n[0]
                n_j = j + n[1]
                if 0 <= n_i <= rows - 1 and 0 <= n_j <= cols - 1 and visited[n_i][n_j] == 0:
                    dfs(grid, n_i, n_j)

        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    dfs(grid, i, j)
                    result += 1

        return result
