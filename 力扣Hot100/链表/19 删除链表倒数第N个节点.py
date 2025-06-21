# 两次遍历，一次遍历得到长度  一次遍历定位前节点 绕过下一个节点
# 时间复杂度 O(N)
# 空间复杂度 O(1)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 先遍历得到长度
        len_n = 0
        cursor = head
        while cursor:
            len_n += 1
            cursor = cursor.next

        # 删除节点 前节点 后节点序号(从1开始)
        del_before, del_cur = len_n - n, len_n - n + 1
        # 1、删除的是头节点
        if len_n - n + 1 == 1:
            return head.next
        # 2、删除的是非头节点
        node_index = 0
        cursor = head
        while cursor:
            node_index += 1
            if node_index == del_before:
                next_node = cursor.next.next if cursor.next else None # 需要考虑删除节点为最后一个节点
                cursor.next = next_node
                break
            cursor = cursor.next

        return head
