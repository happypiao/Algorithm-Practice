# 时间复杂度 O(NlogN)
# 空间复杂度 O(logN) 主要是合并操作创建了虚拟节点

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    链表排序
    采用归并排序的方法
    1、快慢指针进行链表分割
    2、合并两个有序链表
    """

    def splitList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        将链表分割为长度相等的前后连两个链表head、slow，函数仅返回后面slow链表
        :param head:
        :return:
        """
        quick = slow = head
        pre = None
        while quick and quick.next:
            pre = slow
            slow = slow.next
            quick = quick.next.next
        if pre:
            pre.next = None
        return slow

    def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        合并两个有序链表，返回新的链表(递增有序链表)
        思路：通过创建虚拟头节点实现两个有序链表的排序
        :param l1:
        :param l2:
        :return:
        """
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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 递归退出条件，当链表为空或者只有一个节点时直接返回, 否则会无下限循环分割排序
        if head is None or head.next is None:
            return head
        # 1、分割链表
        head2 = self.splitList(head)
        # 2、对两个子链表进行分割排序
        head = self.sortList(head)
        head2 = self.sortList(head2)
        # 3、合并排序
        return self.mergeList(head, head2)
