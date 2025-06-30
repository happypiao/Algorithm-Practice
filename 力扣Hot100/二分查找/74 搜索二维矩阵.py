# 首先找到是哪一行 再在那一行使用二分查找即可
# 时间复杂度 O(logN)
# 空间复杂度 O(1)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows - 1
        while start <= end:
            mid = (start + end) // 2
            s, e = matrix[mid][0], matrix[mid][-1]
            if s <= target <= e:
                return self.searchInsert(matrix[mid], target)
            elif target > e:
                start = mid + 1
            else:
                end = mid - 1

        return False
