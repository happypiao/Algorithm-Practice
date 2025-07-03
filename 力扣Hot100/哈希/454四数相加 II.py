# https://leetcode.cn/problems/4sum-ii/description/
# 时间复杂度 O(n*n)
# 空间复杂度 O(n*n)
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        sum12_map = {}

        # Step 1. 先遍历nums1+nums2和出现的次数
        for n1 in nums1:
            for n2 in nums2:
                sum12_map[n1+n2] = sum12_map.get(n1+n2, 0) + 1

        # Step 2. 遍历nums3 nums4 得到sum34=nums3+nums4 然后判断0-sum34是否在sums12_map中出现
        for n3 in nums3:
            for n4 in nums4:
                free_num = 0 - n3 - n4
                count += sum12_map.get(free_num, 0)

        return count
