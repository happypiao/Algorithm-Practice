# 时间复杂度 O(N)
# 空间复杂度 O(N)
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque()
        dq.append((root, 0))

        result = []
        while dq:
            node, level = dq.popleft()
            if level + 1 == len(result):
                result[level].append(node.val)
            else:
                result.append([node.val])

            if node.left:
                dq.append((node.left, level + 1))
            if node.right:
                dq.append((node.right, level + 1))

        return result
