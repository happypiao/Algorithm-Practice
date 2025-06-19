# 双指针，两端双指针滑动
# 两边指针 哪边矮就移动哪边的指针，因为不管哪边移动，底边宽都会减一，这样优先保证高的一遍不变，移动矮的一遍才可能会遇到更大的
# 时间复杂度 O(N)
# 空间复杂度 O(1)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
