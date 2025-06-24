# 时间复杂度 O(N)
# 空间复杂度 O(H)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 左右子树想反节点比较
        def iseqal(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:

            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and iseqal(left.left, right.right) and iseqal(left.right, right.left)

        return iseqal(root.left, root.right)


# root = TreeNode(1,
#                 left=TreeNode(2, left=None, right=TreeNode(2)),
#                 right=TreeNode(2, left=None, right=TreeNode(2)))
# print(Solution().isSymmetric(root))
