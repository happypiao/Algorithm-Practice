# 通过构建一个空节点链表来实现，简单易于理解
# 时间复杂度 O(N)
# 空间复杂度 O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个临时节点
        tmp_node = ListNode()
        current_cur = tmp_node

        head1, head2 = list1, list2
        while head1 and head2:
            if head1.val <= head2.val:
                current_cur.next = head1
                head1 = head1.next
            else:
                current_cur.next = head2
                head2 = head2.next
            current_cur = current_cur.next

        current_cur.next = head1 or head2

        return tmp_node.next

