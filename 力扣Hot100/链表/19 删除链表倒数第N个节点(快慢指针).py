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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp_node = ListNode(next=head)
        fast_cur, slow_cur = tmp_node, tmp_node

        step = 0
        while fast_cur:
            fast_cur = fast_cur.next
            step += 1
            if step == n + 1:
                while fast_cur:
                    slow_cur = slow_cur.next
                    fast_cur = fast_cur.next
                slow_cur.next = slow_cur.next.next

        return tmp_node.next
