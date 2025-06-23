# 时间复杂度 O(M+N)
# 空间复杂度 O(1)

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_num, col_num = len(matrix), len(matrix[0])

        i, j = 0, col_num - 1
        while 0 <= i < row_num and 0 <= j < col_num:
            root_val = matrix[i][j]
            if root_val == target:
                return True
            elif target > root_val:
                i += 1
            elif target < root_val:
                j -= 1

        return False
