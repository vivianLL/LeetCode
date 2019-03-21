'''
160. Intersection of Two Linked Lists
Easy

https://leetcode.com/problems/intersection-of-two-linked-lists/
Write a program to find the node at which the intersection of two singly linked lists begins.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 法1 暴力法 Time complexity : O(mn) Space complexity : O(1)
        # 法2 哈希表或栈 Time complexity : O(m+n) Space complexity : O(m) or O(n)

        # 法3 双指针 Time complexity : O(m+n) Space complexity : O(1)
        la = 0
        lb = 0
        curA = headA   # 注意重新新建链表，否则改变原链表到结尾
        curB = headB
        while curA:
            la += 1
            curA = curA.next
        while curB:
            lb += 1
            curB = curB.next

        while (la > lb):
            headA = headA.next
            la -= 1
        while (lb > la):
            headB = headB.next
            lb -= 1
        while (headA != headB):
            headA = headA.next
            headB = headB.next
        return headA