from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode], tail: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        pre = tail.next
        cur = head
        while pre != tail:
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 定义一个虚拟空节点
        tmp_node = ListNode(next=head)
        # 定义三个指针
        # pre: 指向子链表上一个节点
        # sub_head: 指向子链表的起始节点
        # sub_tail: 指向子链表的结束节点
        # step_count: 遍历次数，每次遍历k的倍数则开始反转链表
        pre, sub_head, sub_tail = tmp_node, tmp_node.next, tmp_node
        step_count = 0

        while sub_tail:
            sub_tail = sub_tail.next
            # 1、判断sub_tail为空, 即数量不足K则直接返回
            if not sub_tail:
                return tmp_node.next
            step_count += 1
            # 2、次数达到K的倍数，即开始做反转链表操作
            if step_count % k == 0:
                new_head, new_tail = self.reverseList(sub_head, sub_tail)
                # print(new_head.val, new_tail.val)
                # print(pre.val)
                pre.next = new_head
                pre = new_tail
                sub_head = new_tail.next
                sub_tail = new_tail  # 指针指向尾部

        return tmp_node.next

# lists = ListNode(1)
# cur = lists
# for i in [2, 3]:
#     cur.next = ListNode(i)
#     cur = cur.next
#
# print(Solution().reverseKGroup(lists, 2))