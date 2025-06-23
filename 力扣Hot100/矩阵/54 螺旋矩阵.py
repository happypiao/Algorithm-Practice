from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        total_n = m * n
        left, right, up, down = 0, n - 1, 0, m - 1

        result = []
        while len(result) < total_n:
            # 向右
            for i in range(left, right + 1):
                if len(result) < total_n:
                    result.append(matrix[up][i])
            up += 1
            # 向下
            for i in range(up, down + 1):
                if len(result) < total_n:
                    result.append(matrix[i][right])
            right -= 1
            # 向左
            for i in range(right, left - 1, -1):
                if len(result) < total_n:
                    result.append(matrix[down][i])
            down -= 1
            # 向上
            for i in range(down, up - 1, -1):
                if len(result) < total_n:
                    result.append(matrix[i][left])
            left += 1

        return result
