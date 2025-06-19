# 提示：
#
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1
# 时间复杂度 O(N)
# 空间复杂度 O(N)

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 初始化一个前缀和为0， 下标为-1的默认值
        n = len(nums)
        pre_sum = [nums[0]] * n
        for i in range(1, n):
            pre_sum[i] = pre_sum[i-1] + nums[i]
            if pre_sum[i] % k == 0:
                return True

        pre_map = {}
        for j in range(n):
            free = pre_sum[j] % k
            if free in pre_map:
                if j - pre_map[free] >= 2:
                    return True
            else:
                pre_map[free] = j

        return False
