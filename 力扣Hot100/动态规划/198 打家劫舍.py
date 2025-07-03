# 时间复杂度 O(N)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # 动态规划
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # 偷与不偷
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]
