'''
234. Palindrome Linked List
Easy

https://leetcode.com/problems/palindrome-linked-list/
Given a singly linked list, determine if it is a palindrome.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # # 时间复杂度O(N),空间复杂度O(N) 放数组里
        # li = []
        # while head:
        #     li.append(head.val)
        #     head = head.next
        # n = len(li)
        # if n==1:
        #     return True
        # if n%2==0:
        #     if li[:n//2] == li[n//2:][::-1]:
        #         return True
        # else:
        #     if li[:n//2] == li[n//2+1:][::-1]:
        #         return True
        # return False

        # # 快慢指针 时间复杂度O(N),空间复杂度O(N/2)
        # if head==None or head.next==None:
        #     return True
        # slow = fast = head  # #定义快慢指针来确定链表的中点
        # li = []
        # while fast and fast.next:
        #     li.insert(0, slow.val)   #使用队列来模拟栈
        #     print(li)
        #     slow = slow.next
        #     fast = fast.next.next
        # if fast:
        #     slow = slow.next  # 奇数个节点
        # for val in li:
        #     if val != slow.val:
        #         return False
        #     slow = slow.next
        # return True

        # 快慢指针，找到中点后链表反转 时间复杂度O(N),空间复杂度O(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        new_head = self.ReverseList(slow)
        while new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True

    def ReverseList(self,head):
        new_head = None
        while head:
            p = head
            head = head.next   # head = head.next一定要在第二句，而不是最后，要不然就断链了，因为p指向了head更改p相当于更改了head,当head指向next之后，才能更改p
            p.next = new_head
            new_head = p
        return new_head


n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(1)
# n.next.next.next = ListNode(1)

sol = Solution()
ans = sol.isPalindrome(n)
print(ans)
