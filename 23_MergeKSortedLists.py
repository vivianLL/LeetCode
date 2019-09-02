'''
23. Merge k Sorted Lists
Hard

https://leetcode.com/problems/merge-k-sorted-lists/
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''
# Definition for singly-linked list.
from heapq import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists) -> ListNode:
    #     # 归并思想 自己写的
    #     # 时间复杂度O(nlogk) 空间复杂度O(1) 合并两个有序链表的时间复杂度O(n)，k个归并合并O(nlogk)
    #     if not lists:
    #         return None
    #     if len(lists) == 1:
    #         return lists[0]
    #     if len(lists) == 2:
    #         return self.mergeTwoLists(lists[0],lists[1])
    #     middle = len(lists) // 2
    #     left, right = lists[0:middle], lists[middle:]
    #     return self.mergeTwoLists(self.mergeKLists(left), self.mergeKLists(right))
    #
    # def mergeTwoLists(self, l1, l2):
    #     if not l1:
    #         return l2
    #     if not l2:
    #         return l1
    #     if l1.val <= l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2

        # # 暴力法 先把所有链表的值保存到一个list里，对list排序，重构成链表
        # # 时间复杂度O(nlogn) 空间复杂度O(n)
        # self.nodes = []
        # head = point = ListNode(0)
        # for l in lists:
        #     while l:
        #         self.nodes.append(l.val)
        #         l = l.next
        # for x in sorted(self.nodes):
        #     point.next = ListNode(x)
        #     point = point.next
        # return head.next

        # 对全部k个链表从头开始一个个往后比较，可以通过优先队列优化
        # 时间复杂度O(kn) 空间复杂度O(n)/O(1)
        root = cur = ListNode(0)
        h = [(i.val, idx, i) for idx, i in enumerate(lists) if i]
        heapify(h)  # 堆排序
        while h:
            _, idx, node = heappop(h)
            cur.next = node
            cur = cur.next
            if cur.next:
                heappush(h, (cur.next.val, idx, cur.next)) # 将值项推入堆中,保持堆不变

        return root.next

Node1=ListNode(1)
Node1.next=ListNode(4)
Node1.next.next=ListNode(5)
Node2=ListNode(1)
Node2.next=ListNode(3)
Node2.next.next=ListNode(4)
Node3 = ListNode(2)
Node3.next = ListNode(6)
sol = Solution()
sol.mergeKLists([Node1,Node2,Node3])