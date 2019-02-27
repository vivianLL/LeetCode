'''
141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/
Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 集合 时间复杂度O(n) 空间复杂度O(n)
        val = set()
        while head:
            if head not in val:
                val.add(head)  # 注意此处集合中应为链表的结点，而不能只是链表结点的值
            else:
                return True
            head = head.next
        return False

        # 快慢指针 时间复杂度O(n) 空间复杂度O(1)
        fast = head
        slow = head
        while fast and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

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
sol.hasCycle(lNode1)

# 有没有环不能仅靠看有没有重复元素的值判断，还需要判断node.next