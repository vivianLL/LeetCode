'''
21. Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # # 借助列表重新排序，时间复杂度O(nlgn) 空间复杂度O(n)
        # if not (l1 or l2):
        #     return None
        # list1, list2 = [], []
        # while l1:
        #     list1.append(l1)
        #     l1 = l1.next
        # while l2:
        #     list2.append(l2)
        #     l2 = l2.next
        # mylist = (list1 + list2)
        # mylist.sort(key=lambda ListNode: ListNode.val)     # 时间复杂度O(nlgn)，list中放的ListNode对象，需要按ListNode对象的val属性排列.sorted是创建副本，sort改变原值
        # for i in range(len(mylist) - 1):
        #     mylist[i].next = mylist[i + 1]
        # mylist[-1].next = None  # 一定要将原头结点的next设为none
        # return mylist[0]

        # 迭代，借助两个指针
        p = merge = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                merge.next = l1
                l1 = l1.next
            else:
                merge.next = l2
                l2 = l2.next
            merge = merge.next
        merge.next= l1 or l2  # 注意：当由于其中一链表l1或者l2为空导致跳出while循环时，还需要将另一不为null的链表的后续部分赋给合并链表。
        return p.next

        # 递归
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


lNode1=ListNode(1)
lNode2=ListNode(2)
lNode3=ListNode(4)
Node1=ListNode(1)
Node2=ListNode(3)
Node3=ListNode(4)
lNode1.next=lNode2
lNode2.next=lNode3
Node1.next=Node2
Node2.next=Node3
sol = Solution()
sol.mergeTwoLists(lNode1,Node1)

# 思路：初始化两个链表头，其中一个表头用以记录两个单调递增链表比较后的结果，另一个用以返回结果。
# 用while循环：
# ①如果两个链表不为空，比较进行，并将小的那个赋给合并的链表头。小表头继续走一步，合并表头继续走一步。
# ②如果两个链表有其一为空，那么跳出循环，并将另一不为null的链表的后续部分赋给合并链表。
