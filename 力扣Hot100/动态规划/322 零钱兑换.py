import sys
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 使用一维数组, dp[i] amount为i的最少硬币个数
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        # 遍历
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j - coin] + 1, dp[j])

        return -1 if dp[amount] == sys.maxsize else dp[-1]
