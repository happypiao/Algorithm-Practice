# 快慢指针
# 时间复杂度 O(N)
# 空间复杂度 O(1)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 快慢指针的方法
        quick, slow = head, head

        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
            if slow == quick:
                return True

        return False
