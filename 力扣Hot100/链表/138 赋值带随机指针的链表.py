# 时间复杂度 O(N)
# 空间复杂度 O(N)

from typing import Optional


# Definition for a Node.

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 赋值节点主要是要知道random, 可以使用字典保存新旧节点的对照关系。
        # 一次遍历只能吧所有节点创建出来，random指向节点无法再次找到
        # 所以先一次遍历创建所有独立的节点，再次遍历来构建新节点的关联关系
        # 1 第一次遍历 创建所有新节点
        node_map = {}
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next

        # 2 第二次遍历构建next random
        current = head
        while current:
            new_node = node_map[current]
            new_node.next = node_map.get(current.next, None)
            new_node.random = node_map.get(current.random, None)
            current = current.next

        # 原链表可能为空
        return node_map.get(head, None)
