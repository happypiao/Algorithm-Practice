# 双指针
# 时间复杂度 O(N)
# 空间复杂度 O(1)
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head

        while cur:
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next

        return pre
