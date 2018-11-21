'''
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given a linked list, remove the n-th node from the end of list and return its head.
'''

# 40ms
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = head
        org = head

        for i in range(1, n):
            start = start.next
            i = i + 1

        while start.next != None:
            start = start.next
            org = org.next

        # 删除该节点 分情况讨论
        head_node = head
        del_node = org

        if not (head_node and del_node):
            return False

        if del_node.next:
            # 删除的节点不是尾节点，而且不是唯一一个节点
            del_next_node = del_node.next
            del_node.val = del_next_node.val
            del_node.next = del_next_node.next
            del_next_node.val = None
            del_next_node.next = None

        elif del_node == head_node:
            # 唯一一个节点，删除头节点
            head_node = None
            del_node = None

        else:
            # 删除节点为尾节点
            node = head_node
            while node.next != del_node:
                node = node.next

            node.next = None
            del_node = None

        return head_node


lNode1=ListNode(1)
lNode2=ListNode(2)
lNode3=ListNode(3)
lNode4=ListNode(4)
lNode5=ListNode(5)
lNode1.next=lNode2
lNode2.next=lNode3
lNode3.next=lNode4
lNode4.next=lNode5
sol = Solution()
sol.removeNthFromEnd(lNode1,1)

# 基本思路：遍历一次链表获得链表长度，再次遍历链表，至n-k+1出输出
# 进阶思路：设置2个指针，第一个指针走K步之后，第二个指针开始从头走，这样两个指针之间始终相隔K，当指针2走到链表结尾时，指针1的位置即倒数K个节点
# 问题分解：1.先找倒数第n个节点 2.删除该节点