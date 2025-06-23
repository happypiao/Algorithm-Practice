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

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        dq = deque()
        dq.append((root, 0))
        max_depth = 0

        while dq:
            node, depth = dq.popleft()
            cur_depth = depth + 1
            max_depth = max(max_depth, cur_depth)
            if node.left:
                dq.append((node.left, cur_depth))
            if node.right:
                dq.append((node.right, cur_depth))

        return max_depth
