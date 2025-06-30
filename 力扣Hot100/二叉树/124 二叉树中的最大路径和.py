from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = 0
        if root is None:
            return 0

        def preorder_dfs(root: Optional[TreeNode], pre_sum: int) -> int:
            nonlocal max_path_sum
            if not root:
                return pre_sum
            pre_sum = pre_sum + root.val
            left_sum = preorder_dfs(root.left, pre_sum)
            right_sum = preorder_dfs(root.right, pre_sum)
            max_path_sum = max(max_path_sum, left_sum + right_sum - root.val)
            return max(left_sum, right_sum)

        preorder_dfs(root, 0)
        return max_path_sum
