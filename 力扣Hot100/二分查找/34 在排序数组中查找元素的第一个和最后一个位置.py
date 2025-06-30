# 时间复杂度O(Logn)
from typing import List


class Solution:

    def get_right_boarder(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        right_boarder = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                right_boarder = mid
                left = mid + 1
            else:
                left = mid + 1

        return right_boarder

    def get_left_boarder(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        left_boarder = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left_boarder = mid
                right = mid - 1
            else:
                left = mid + 1

        return left_boarder

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.get_left_boarder(nums, target),
                self.get_right_boarder(nums, target)]
