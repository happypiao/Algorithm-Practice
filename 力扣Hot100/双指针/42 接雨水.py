from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        nums = len(height)
        # 柱子数小于2 直接返回0
        if nums <= 2:
            return 0

        # 参考前缀和思想，记录柱子左、右两侧最高的柱子高度
        left_max = [0]
        for i in range(1, nums):
            left_max.append(max(height[i - 1], left_max[-1]))

        right_max = [0] * nums
        for j in range(nums - 2, -1, -1):
            right_max[j] = max(height[j + 1], right_max[j + 1])

        # 遍历柱子 求接雨水面积
        sum_ = 0
        for k in range(0, nums):
            count = min(left_max[k], right_max[k]) - height[k]
            if count > 0:
                sum_ += count

        return sum_

