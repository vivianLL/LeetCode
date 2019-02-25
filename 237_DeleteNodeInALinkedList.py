'''
237. Delete Node in a Linked List

https://leetcode.com/problems/delete-node-in-a-linked-list/
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.O(1) time
Given linked list -- head = [4,5,1,9], which looks like following: 4->5->1->9
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

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
sol.deleteNode(lNode4)
