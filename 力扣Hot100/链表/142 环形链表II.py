
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        quick, slow = head, head

        # while quick and quick.next:
        #     quick = quick.next.next
        #     slow = slow.next
        #     if quick == slow:
        #         start1 = quick
        #         start2 = head
        #         while start1 != start2:
        #             start1 = start1.next
        #             start2 = start2.next
        #         return start1
        #
        # return None

        node_map = set()
        temp_head = head
        while temp_head:
            if temp_head in node_map:
                return temp_head
            node_map.add(temp_head)
            temp_head = temp_head.next

        return None
