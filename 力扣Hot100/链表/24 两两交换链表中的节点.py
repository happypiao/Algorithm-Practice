# 时间复杂度 O(N)
# 空间复杂度 O(1)
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头结点，每次虚拟头结点需要指向需要交换节点的头一个节点
        # 虚拟头结点 指向第二个节点 第二个节点指向第一个节点 第一个节点指向后面，依次循环
        null_node = ListNode(next=head)
        current = null_node

        while current.next and current.next.next:
            # 1、首先获取后面三个节点的位置
            after_first_node = current.next
            after_second_node = current.next.next
            after_third_node = current.next.next.next
            # 2、交换current后面两个节点的位置
            current.next = after_second_node
            after_second_node.next = after_first_node
            after_first_node.next = after_third_node
            # 3、current位置向后移动两位
            current = current.next.next

        return null_node.next
