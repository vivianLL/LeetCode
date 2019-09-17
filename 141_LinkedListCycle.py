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
        # # 集合 时间复杂度O(n) 空间复杂度O(n)
        # val = set()
        # while head:
        #     if head not in val:
        #         val.add(head)  # 注意此处集合中应为链表的结点，而不能只是链表结点的值
        #     else:
        #         return True
        #     head = head.next
        # return False

        # 快慢指针 时间复杂度O(n) 空间复杂度O(1)
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
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
ans = sol.hasCycle(lNode1)
print(ans)

# 参考网址：https://www.cnblogs.com/hiddenfox/p/3408931.html
