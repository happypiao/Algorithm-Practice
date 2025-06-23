# 时间复杂度 O(MN)
# 空间复杂度 O(M)
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_l = len(matrix)
        col_l = len(matrix[0])
        # 1. 遍历 找出为0的行，同时修改行的值 记录列的index
        list_cols = set()
        for row_index, row in enumerate(matrix):
            for col_index, col in enumerate(row):
                if col == 0:
                    list_cols.add(col_index)
                    matrix[row_index] = [0] * col_l

        # 2. 修改列的值为0
        for col_index in list_cols:
            for row_index in range(row_l):
                matrix[row_index][col_index] = 0
