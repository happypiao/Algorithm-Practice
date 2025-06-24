# 时间复杂度 O(N)
# 空间复杂度 O(1)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(root: Optional[TreeNode], targetSum: int) -> bool:
            if not root.left and not root.right:
                return targetSum == 0
            if root.left and dfs(root.left, targetSum - root.left.val):
                return True
            if root.right and dfs(root.right, targetSum - root.right.val):
                return True
            return False

        return dfs(root, targetSum - root.val)
