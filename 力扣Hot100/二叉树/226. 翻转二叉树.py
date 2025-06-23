# 时间复杂度 O(N)
# 空间复杂度 O(N)

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        dq = deque()
        dq.append(root)

        while dq:

            node = dq.popleft()
            if not node:
                continue
            node_right = node.right
            node.right = node.left
            node.left = node_right
            dq.append(node.left)
            dq.append(node.right)

        return root
