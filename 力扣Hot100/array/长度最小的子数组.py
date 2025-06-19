import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = 0
        left_i, right_j = 0, 0
        min_length = sys.maxsize

        while right_j < len(nums):
            current_sum += nums[right_j]

            while current_sum >= target:
                min_length = min(right_j - left_i + 1, min_length)
                current_sum -= nums[left_i]
                left_i += 1

            right_j += 1

        return min_length
