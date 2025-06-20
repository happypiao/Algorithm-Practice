# 接雨水思路
# 1、最左侧 和 最右侧柱子是接不住水的，以为他们有一边没有柱子
# 2、每个柱子可以接的雨水等于左边最高的柱子和右边最高柱子 两者区最小值，再减去当前柱子高度。如果这个差值大于0则是可以接到水
# 3、累加所有柱子可以接的雨水总和
# 时间复杂度 O(N)
# 空间复杂度 O(N)
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        # 1、求每个柱子左边的最高柱子的高度
        left_max = [0] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i - 1])

        # 2、求每个柱子右边的最高柱子的高度
        right_max = [0] * n
        for j in range(n - 2, -1, -1):
            right_max[j] = max(right_max[j + 1], height[j + 1])

        # 3、累加每个柱子接的雨水量
        sum_water = 0
        for i in range(0, n):
            water = min(left_max[i], right_max[i]) - height[i]
            if water > 0:
                sum_water += water

        return sum_water
