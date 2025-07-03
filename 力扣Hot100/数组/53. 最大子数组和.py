import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_pre_sum = 0
        pre_sum = 0
        max_sum = -sys.maxsize

        for n in nums:
            pre_sum += n
            max_sum = max(max_sum, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)

        return max_sum
