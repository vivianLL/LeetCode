'''
83. Remove Duplicates from Sorted List

https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Given a sorted linked list, delete all duplicates such that each element appear only once.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 定义两个指针相比较，遇到重复的删去 时间复杂度O(n）
        if not head:
            return head
        temp = head

        while temp:
            nex = temp.next
            while nex and nex.val == temp.val:
                nex = nex.next  # 删除重复结点
            temp.next = nex
            temp = temp.next
        return head


        # 另一种写法
        if not head:
            return []
        i = head
        j = head
        while j.next != None:
            j = j.next
            # if i.value ==j.value:
            #     j = j.next
            if i.val != j.val:
                i.next = j
                i = i.next
            elif i.val == j.val and j.next == None:
                i.next = None
        return head

        # 时间复杂度O(n），不借助另外链表
        if not head:
            return None
        cur_List = head
        while cur_List.next:
            if cur_List.val == cur_List.next.val:
                cur_List.next = cur_List.next.next   # 注意此处多了一个next，以删除当前的下一个链表结点
            else:
                cur_List = cur_List.next
        return head


# 注意：一定注意不要改变头结点，否则无法返回head