# 时间复杂度 O(N)
# 空间复杂度 O(1)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    左右子树深度的最大值
    """
    max_len = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def query_depth(root: Optional[TreeNode]):
            if root is None:
                return 0
            left_depth = query_depth(root.left)
            right_depth = query_depth(root.right)
            self.max_len = max(self.max_len, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        query_depth(root)
        return self.max_len
