# 时间复杂度 O(N)
# 空间复杂度 O(M)
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 符合条件的子数组数量
        count = 0
        # 前缀和
        pre_sum = 0
        # 适用字典记录前缀和相同的子数组的数量
        pre_sum_map = {0: 1}

        # 遍历数组， 判断pre_sum - k是否存在于pre_sum_map中
        for num in nums:
            pre_sum += num
            if pre_sum - k in pre_sum_map:
                count += pre_sum_map.get(pre_sum - k, 0)
            pre_sum_map[pre_sum] = pre_sum_map.get(pre_sum, 0) + 1

        return count
