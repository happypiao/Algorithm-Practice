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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 广度遍历 层级遍历 取最右边的值
        result = []
        if not root:
            return []

        dq = deque()
        dq.append(root)

        while dq:
            val = None
            for _ in range(len(dq)):
                node = dq.popleft()
                val = node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            if val is not None:
                result.append(val)

        return result
