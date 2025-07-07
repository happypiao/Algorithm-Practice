from typing import List, Optional


class TreeNode(object):
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None


class TreeUtils(object):
    """
    二叉树工具类
    """

    def __init__(self):
        self.result = []

    def gen_tree(self, preorder: List[str], inorder: List[str]) -> Optional[TreeNode]:
        """
        依据前序遍历 中序遍历构造二叉树
        :param inorder:
        :param preorder:
        :return:
        """
        if not preorder or not inorder:
            return None
        # 1、获取父节点
        root_val = preorder[0]
        root_index = inorder.index(root_val)
        # 2、获取左右子节点（子树），构造二叉树
        new_node = TreeNode(root_val)
        new_node.left = self.gen_tree(preorder[1: root_index + 1], inorder[:root_index])
        new_node.right = self.gen_tree(preorder[root_index + 1:], inorder[root_index + 1:])

        return new_node

    def dfs_after_order(self, root: Optional[TreeNode]):
        """
        后序遍历二叉树
        :param root:
        :return:
        """
        if not root:
            return
        self.dfs_after_order(root.left)
        self.dfs_after_order(root.right)
        self.result.append(root.val)

    def solve_method(self, preorder: List[str], inorder: List[str]):
        """
        根据前序遍历 中序遍历 得到后序遍历结果
        :param preorder:
        :param inorder:
        :return:
        """
        # 1、根据前序遍历 中序遍历构造一颗新的二叉树
        new_tree = self.gen_tree(preorder, inorder)
        # 2、对新的二叉树进行后序遍历
        self.dfs_after_order(new_tree)

        return self.result


if __name__ == "__main__":
    print(''.join(TreeUtils().solve_method(list("DBACEGF"), list("ABCDEFG"))))
