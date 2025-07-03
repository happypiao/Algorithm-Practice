import sys
from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = sys.maxsize
        n = len(nums)

        for i in range(n - l + 1):
            s = 0
            for j in range(i, min(i + r, n)):
                s += nums[j]
                if j - i + 1 >= l and s > 0:
                    min_sum = min(min_sum, s)

        return min_sum if min_sum != sys.maxsize else -1
