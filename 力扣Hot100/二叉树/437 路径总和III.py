# 时间复杂度 O(N*N)
# 空间复杂度 O(N)
# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.count = 0

    def dfs(self, root: Optional[TreeNode], targetSum: int):
        if targetSum == 0:
            self.count += 1

        if root.left:
            self.dfs(root.left, targetSum - root.left.val)
        if root.right:
            self.dfs(root.right, targetSum - root.right.val)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        dq = deque()
        dq.append(root)

        while dq:
            node = dq.popleft()
            self.dfs(node, targetSum - node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        return self.count
