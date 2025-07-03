"""
# 题目：128 最长连续序列
https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 既然时间复杂度是O(n) 就不能使用排序对nums排序后用双指针的方法了
        # 那就只能遍历一遍 遍历一遍就得看他的i+1 或者i=1都存在，判断是否存在O(1)的就用哈希集合
        # 考虑到连续子序列长度从最小值开始寻找，可以避免重复哈希判断
        nums_set = set(nums)
        max_len = 0

        for item in nums_set:   # 主意此处遍历对象为nums_set, 因为nums可能会有大量的重复元素

            # 判断条件，如果存在-1的数，则跳过，直到找到某个连续序列的最小是
            if item - 1 in nums_set:
                continue

            # 当前序列默认为1
            current_len = 1
            current_num = item
            # item则为某个序列的最小值
            while current_num + 1 in nums_set:
                current_len += 1
                current_num += 1

            max_len = max(max_len, current_len)

        return max_len
