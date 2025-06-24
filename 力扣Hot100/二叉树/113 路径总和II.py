# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 叶子节点 是指没有子节点的节点。
# 时间复杂度 O(N)
# 空间复杂度 O(N)
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        paths = []

        def preorder(root: Optional[TreeNode], targetSum: int, path: List[int]):
            if not root.left and not root.right:
                if targetSum == 0:
                    paths.append(path)
                return

            if root.left:
                preorder(root.left, targetSum - root.left.val, path + [root.left.val])
            if root.right:
                preorder(root.right, targetSum - root.right.val, path + [root.right.val])

        preorder(root, targetSum - root.val, [root.val])
        return paths
