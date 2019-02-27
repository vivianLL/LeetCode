'''
206. Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/
Reverse a singly linked list.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 借助列表，时间复杂度O(n) 空间复杂度O(n)
        if not head:
            return None
        mylist = []
        while head:
            mylist.append(head)
            head = head.next
        mylist = mylist[::-1]
        for i in range(len(mylist) - 1):
            mylist[i].next = mylist[i + 1]
        mylist[-1].next = None  # 一定要将原头结点的next设为none
        return mylist[0]

        # 迭代 时间复杂度O(n) 空间复杂度O(1)
        pre = None
        cur = head
        while cur != None:
            lat = cur.next
            cur.next = pre
            pre = cur
            cur = lat
        return pre

        # 递归 时间复杂度O(n) 空间复杂度O(1)
        if head == None or head.next == None:  #空链表或只有一个节点的情况
            return head
        node = self.reverseList(head.next)
        head.next.next = head                  # 递归到尾节点时，则令尾节点的next为头结点None，并指向原尾节点
        head.next = None
        return node

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
sol.reverseList(lNode1)

# 思路：
# 迭代：设置pre,cur,lat三个指针，首先cur.next = pre，接着pre = cur，cur = lat，lat = lat.next，重复上述操作直到lat=None，最后cur.next = pre。
# 递归：因为reverseList(head)返回输入的链表反转后的head，所以先reverseList(head.next)递归到最后一个结点，再head.next.next=head，head.next=None，返回node即可。
# 参考网址：https://blog.csdn.net/qq_17550379/article/details/80647926