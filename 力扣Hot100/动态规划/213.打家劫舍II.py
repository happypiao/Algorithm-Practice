# 时间复杂度 O(N)
from typing import List


class Solution:

    def rob_range(self, nums: List[int], start: int, end: int):
        n_size = end - start + 1
        if n_size == 0:
            return 0
        if n_size == 1:
            return nums[start]
        dp = [0] * n_size
        dp[0] = nums[start]
        dp[1] = max(nums[start], nums[start + 1])

        for i in range(2, n_size):
            dp[i] = max(dp[i - 2] + nums[start + i], dp[i - 1])

        return dp[-1]

        pass

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(self.rob_range(nums, 1, len(nums) - 1), self.rob_range(nums, 0, len(nums) - 2))
