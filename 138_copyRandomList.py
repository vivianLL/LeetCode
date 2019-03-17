'''
138. Copy List with Random Pointer
Medium

https://leetcode.com/problems/copy-list-with-random-pointer/
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
'''
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # # 剑指offer方法二 时间空间复杂度O(n)
        # # 把N`链接在N的后面
        # node = head                   # head是不变的，node和clone一直在移动
        # while node:
        #     clone = Node(node.val,node.next,None)
        #     node.next = clone
        #     node = clone.next
        #
        # # 设置复制出来的节点random
        # node = head
        # while node:
        #     clone = node.next         # 从第二个开始，即从新复制的链表头开始
        #     if node.random != None:
        #         clone.random = node.random.next
        #     node = clone.next         # 两次next
        #
        # # 按奇偶拆成两个链表
        # node = head
        # clonehead = None
        # clonenode = None
        # if node:
        #     clonehead = clonenode = node.next   # 找到新复制的链表头，
        #     node.next = clonenode.next
        #     node = node.next                    # 找到拆开后的下一个（未拆开前的下一个的下一个）
        # while node:
        #     clonenode.next = node.next          #node和clonenode分别拆开
        #     clonenode = clonenode.next
        #     node.next = clonenode.next
        #     node = node.next
        # return clonehead

        if head is None:
            return None
        copied = dict()   # 新建字典（哈希表）
        node = head
        while node is not None:                  # 先复制链表的值
            node_copy = Node(node.val, None, None)
            copied[node] = node_copy
            node = node.next

        node = head
        while node is not None:                  # 再分别复制链表的next和random
            if node.next is None:
                copied[node].next = None
            else:
                copied[node].next = copied[node.next]
            if node.random is None:
                copied[node].random = None
            else:
                copied[node].random = copied[node.random]
            node = node.next

        return copied[head]

