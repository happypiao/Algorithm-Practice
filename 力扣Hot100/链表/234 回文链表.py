# 先遍历链表得到所有val
# 再使用列表切片判断和原vals的值是否相等
# 时间复杂度 O(N)
# 空间复杂度 O(1)

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        tmp_head = head

        while tmp_head:
            vals.append(tmp_head.val)
            tmp_head = tmp_head.next

        return vals == vals[::-1]
