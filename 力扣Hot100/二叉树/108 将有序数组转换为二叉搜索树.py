# 时间复杂度 O(N)
# 空间复杂度 O(N)

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def gen_tree(self, nums: List[int], left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        mid_index = (left + right) // 2
        new_root = TreeNode(nums[mid_index])
        new_root.left = self.gen_tree(nums, left, mid_index - 1)
        new_root.right = self.gen_tree(nums, mid_index + 1, right)
        return new_root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.gen_tree(nums, 0, len(nums) - 1)
