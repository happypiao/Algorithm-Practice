# Definition for singly-linked list.
from typing import Optional
# 需要使用一个哈希表记录第一个链表 每个链表节点的id值，如果有相交 第一节点的id值是一样的
# 优化方法 空间复杂度O(1)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     node_map = {}
    #     head = headA
    #     while head:
    #         node_map[id(head)] = head.val
    #         head = head.next
    #
    #     head = headB
    #     find = False
    #     while head:
    #         if id(head) in node_map:
    #             find = True
    #             break
    #         head = head.next
    #
    #     return head if find else None
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 定义一个求链表长度的内部函数
        def get_len(node: ListNode) -> int:
            list_len = 0
            while node:
                list_len += 1
                node = node.next
            return list_len

        head_a, head_b = headA, headB
        len_a, len_b = get_len(head_a), get_len(head_b)

        # 需要重置head_a head_b
        head_a, head_b = headA, headB

        # 判断长度， 保证head_a长度小于head_b
        if len_a > len_b:
            len_a, len_b = len_b, len_a
            head_a, head_b = head_b, head_a

        # 将head_b指针移动到len_b - len_a个位置
        for _ in range(len_b - len_a):
            head_b = head_b.next

        # 同步遍历两个链表，当两个链表节点相同时，直接返回
        while head_a and head_b:
            if head_a == head_b:
                return head_a
            head_b = head_b.next
            head_a = head_a.next

        return None