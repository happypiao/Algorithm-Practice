# 时间复杂度 O(N)
# 空间复杂度 O(N)
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        node_list = []

        def preorder(root: Optional[TreeNode]):
            if not root:
                return
            node_list.append(root)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        for i in range(1, len(node_list)):
            pre = node_list[i - 1]
            cur = node_list[i]
            pre.left = None
            pre.right = cur
