# 回溯法 来解决
# 时间复杂度 O(N)
# 空间复杂度 O(N)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def afterorder(root: 'TreeNode'):
            if not root:
                return None
            if root == p or root == q:
                return root
            # 左子树
            left = afterorder(root.left)
            # 右子树
            right = afterorder(root.right)
            # 父节点
            if left is None and right is not None:
                return right
            elif left is not None and right is None:
                return left
            elif left is not None and right is not None:
                return root
            else:
                return None

        return afterorder(root)
