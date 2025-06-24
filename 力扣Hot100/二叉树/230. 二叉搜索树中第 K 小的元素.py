from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = -1

        def dfs(root: Optional[TreeNode]) -> None:
            nonlocal k, result
            if root is None:
                return

            dfs(root.left)
            k -= 1
            if k == 0:
                result = root.val
            dfs(root.right)

        dfs(root)

        return result
