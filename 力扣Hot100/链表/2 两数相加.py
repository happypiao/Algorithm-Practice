from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个空的链表头
        tmp_node = ListNode()
        cur_node = tmp_node
        # 默认向上进位数为0
        up_num = 0

        # 遍历两个链表的节点
        while l1 or l2:
            # 获取链表当前节点的val
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            # 计算总和
            sum_l1_l2 = l1_val + l2_val + up_num
            # 计算余数，余数保留在下个节点
            node_val = sum_l1_l2 % 10
            # 进位，整数得到向上进位的数
            up_num = sum_l1_l2 // 10
            # 创建cur_node.next节点
            cur_node.next = ListNode(node_val)
            # 指针向后移动
            cur_node = cur_node.next
            l1 = l1.next
            l2 = l2.next

        # 处理进位数
        if up_num:
            cur_node.next = ListNode(up_num)

        return tmp_node.next
