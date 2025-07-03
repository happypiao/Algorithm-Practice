# 多次反转即可
# 时间复杂度：O(n)，其中 n 是 nums 的长度。
# 空间复杂度：O(1)。
from typing import List


class Solution:

    def reverse_list(self, nums: List[int], start_i:int, end_j:int) -> None:
        while start_i < end_j:
            nums[start_i], nums[end_j] = nums[end_j], nums[start_i]
            start_i += 1
            end_j -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)

        # 考虑到 会出现刚好反转次数为数组长度整数倍，则无需翻转
        k = k % nums_len
        if k == 0:
            return

        self.reverse_list(nums, 0, nums_len - 1)
        self.reverse_list(nums, 0, k - 1)
        self.reverse_list(nums, k, nums_len - 1)

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     n = len(nums)
    #     # 计算有效的次数
    #     k = k % n
    #     # 原地切片即原地修改
    #     nums[:] = nums[-k:] + nums[0:-k]



