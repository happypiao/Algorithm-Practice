# 时间复杂度 O(NlogN)
# 空间复杂度 O(logN) 主要是合并操作创建了虚拟节点
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeLists(self, l1: Optional[ListNode], l2: Optional[ListNode] ) -> Optional[ListNode]:
        tmp_node = ListNode()
        cur = tmp_node
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2

        return tmp_node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None

        len_n = len(lists)
        lists1 = lists[: len_n // 2]
        lists2 = lists[len_n // 2: len_n]
        l1 = self.mergeKLists(lists1)
        l2 = self.mergeKLists(lists2)
        return self.mergeLists(l1, l2)
