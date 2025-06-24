# 时间复杂度 O(N)
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
        self.targetSum = 0
        self.pre_sum = {0: 1}

    def dfs(self, root: Optional[TreeNode], preSum: int):
        if not root:
            return

        preSum += root.val
        if preSum - self.targetSum in self.pre_sum:
            self.count += self.pre_sum[preSum-self.targetSum]
        self.pre_sum[preSum] = self.pre_sum.get(preSum, 0) + 1
        self.dfs(root.left, preSum)
        self.dfs(root.right, preSum)
        self.pre_sum[preSum] -= 1

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        self.targetSum = targetSum
        self.dfs(root, 0)
        return self.count
