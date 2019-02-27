'''
92. Reverse Linked List II
Medium

https://leetcode.com/problems/reverse-linked-list-ii/
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # # 借助列表，时间复杂度O(n) 空间复杂度O(n)
        # if not head:
        #     return None
        # mylist = []
        # while head:
        #     mylist.append(head)
        #     head = head.next
        # if m < 2:                 # 防止m-2小于零越界
        #     mylist[m - 1:n] = mylist[n - 1::-1]
        # else:
        #     mylist[m - 1:n] = mylist[n - 1:m - 2:-1]
        # for i in range(len(mylist) - 1):
        #     mylist[i].next = mylist[i + 1]
        # mylist[-1].next = None  # 一定要将原头结点的next设为none
        # return mylist[0]


        # # 迭代 时间复杂度O(n) 空间复杂度O(1)
        # if not head:
        #     return None
        # cur = head
        # pre = None
        # while m > 1:
        #     pre = cur
        #     cur = cur.next
        #     m, n = m - 1, n - 1
        #
        # tail, con = cur, pre    # 记录反转的起点处的前后两个结点
        #
        # while n:                # 反转结点直到n等于0
        #     lat = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = lat
        #     n -= 1
        #
        # if con:                 # 连接上开始反转处
        #     con.next = pre
        # else:
        #     head = pre
        # tail.next = cur
        # return head


        # # 递归 官方solution 时间复杂度O(n) 空间复杂度O(1)
        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop        # nonlocal定义在闭包里

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head

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
sol.reverseBetween(2,4)