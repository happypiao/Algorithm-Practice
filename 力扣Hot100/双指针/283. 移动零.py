from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left_i, right_j = 0, 0

        while right_j < n:
            if nums[right_j] != 0:
                nums[left_i], nums[right_j] = nums[right_j], nums[left_i]
                left_i += 1
            right_j += 1
