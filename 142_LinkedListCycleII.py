'''
142. Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 集合 时间复杂度O(n) 空间复杂度O(n)
        val = set()
        while head:
            if head not in val:
                val.add(head)  # 注意此处集合中应为链表的结点，而不能只是链表结点的值
            else:
                # print(len(list(val))-1)
                return head
            head = head.next
        return None

        # # 快慢指针 时间复杂度O(n) 空间复杂度O(1)
        if not head:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != head:  # 当两指针相遇且不为头结点时，环内指针和头指针同时每步移动一个节点，
                    head = head.next
                    slow = slow.next

                return slow
        # fast = head
        # slow = head
        # while fast and fast.next != None:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         return True
        # return False

lNode1=ListNode(1)
lNode2=ListNode(2)
lNode3=ListNode(3)
lNode4=ListNode(4)
lNode5=ListNode(1)
lNode1.next=lNode2
lNode2.next=lNode3
lNode3.next=lNode4
lNode4.next=lNode5
lNode5.next=lNode1
sol = Solution()
ans = sol.detectCycle(lNode1)
print(ans)
