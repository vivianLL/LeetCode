'''
876. Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        if fast == None:  # 空链表的情况
            return None
        while fast.next != None:
            if fast.next.next != None:
                fast = fast.next.next
                slow = slow.next
            else:                  # 偶数个元素最后一步没有fast.next.next的情况
                fast = fast.next
                slow = slow.next
        return slow


lNode1 = ListNode(1)
lNode2 = ListNode(2)
lNode3 = ListNode(3)
lNode4 = ListNode(4)
lNode5 = ListNode(5)
lNode6 = ListNode(6)
lNode1.next = lNode2
lNode2.next = lNode3
lNode3.next = lNode4
lNode4.next = lNode5
lNode5.next = lNode6
sol = Solution()
ans = sol.middleNode(lNode1)
print(ans)