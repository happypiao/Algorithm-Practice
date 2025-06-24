# 时间复杂度 O(N)
# 空间复杂度 O(1)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    pre = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.isValidBST(root.left)
        if self.pre and self.pre.val >= root.val:
            return False
        self.pre = root
        right = self.isValidBST(root.right)
        return left and right
