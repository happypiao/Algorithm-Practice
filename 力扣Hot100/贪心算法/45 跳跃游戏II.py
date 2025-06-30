# 时间复杂度O(N)
# 空间复杂度O(1)
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step_count = 0
        i = 0
        cur_cover = 0
        next_cover = 0
        while i <= next_cover:
            next_cover = max(next_cover, i + nums[i])
            if i == cur_cover:
                if i != len(nums) - 1:
                    step_count += 1
                    cur_cover = next_cover
                    if next_cover >= len(nums) - 1:
                        break
                else:
                    break
            i += 1

        return step_count
