# 时间复杂度O(N)
# 空间复杂度O(1)
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        i, max_step = 0, 0
        while i <= max_step:
            max_step = max(max_step, i + nums[i])
            if i == len(nums) - 1:
                return True
            i += 1

        return False
