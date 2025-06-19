# 时间 O(N)
# 空间 O(N)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        pre_nums = [1] * length
        for i in range(1, length):
            pre_nums[i] = pre_nums[i - 1] * nums[i - 1]

        suf_nums = [1] * length
        for i in range(length - 2, -1, -1):
            suf_nums[i] = suf_nums[i + 1] * nums[i + 1]

        result = []
        for i in range(length):
            result.append(suf_nums[i] * pre_nums[i])

        return result
