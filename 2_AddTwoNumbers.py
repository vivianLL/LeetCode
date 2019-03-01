'''
2. Add Two Numbers
Medium

https://leetcode.com/problems/add-two-numbers/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # # 自写程序 先把和用列表表示出来，再变成链表
        # list1 = []
        # list2 = []
        # while l1!=None:
        #     list1.append(l1.val)
        #     l1 = l1.next
        # while l2!=None:
        #     list2.append(l2.val)
        #     l2 = l2.next
        # print(list1,list2)
        # len1,len2 = len(list1),len(list2)
        # if len1>len2:
        #     list2.extend([0]*(len1-len2))
        # else:
        #     list1.extend([0] * (len2 - len1))   # 在高位补零，使两个数的列表长度相等
        # sum = []
        # add = 0
        # for i in range(len(list1)):
        #     if int(list1[i]) + int(list2[i]+add) < 10:   # 注意：有没有下一位的进位是看两数与本位进位之和
        #         sum.append(int(list1[i]) + int(list2[i]) + add)
        #         add = 0
        #     else:
        #         sum.append(int(list1[i]) + int(list2[i]) - 10 + add)
        #         add = 1
        # if add == 1:     # 最高位如有进位需要补一位
        #     sum.append(1)
        # print(sum)
        # lNode = ListNode(sum[0])
        # lNode1 =lNode
        # for i in range(1, len(sum)):
        #     lNode1.next = ListNode(sum[i])
        #     lNode1 = lNode1.next
        # return lNode

        # 直接用链表相加
        # 一开始不做l1和l2的非空判断，因为题中已经说明是非空链表
        # 记录是否需要增加新节点，或者在链表的下一个节点是否需要加1，同时记录两个链表同级节点的和
        carry = 0

        # 这里的执行顺序是 res = ListNode(0),pre = res
        res = pre = ListNode(0)

        # 判断l1、l2、carry是否有值，carry有值的话需要增加节点，或者在链表下一个节点加1
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            # carry现在是同级节点的和
            # divmod返回商与余数的元组，分为carry和val
            # caarry不是0的话，需要新建节点或者在链表的下一个节点加1 ，在循环中用到
            carry, val = divmod(carry, 10)

            # 新建链表节点
            # 执行顺序是pre.next = ListNode(val)
            # pre = pre.next
            pre.next = pre = ListNode(val)

        # res等价于pre ,res.val = 0，所以返回res.next
        return res.next

        # 简洁写法
        dummy, carry, n1, n2 = ListNode(0), 0, l1, l2
        node = dummy
        while n1 or n2 or carry:
            n1_val = 0 if not n1 else n1.val
            n2_val = 0 if not n2 else n2.val
            s = n1_val + n2_val + carry
            carry, s = divmod(s, 10)     # 把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)。
            node.next = ListNode(s)
            node = node.next
            if n1: n1 = n1.next
            if n2: n2 = n2.next
        return dummy.next


# lNode1=ListNode(2)
# lNode2=ListNode(4)
# lNode3=ListNode(3)
# Node4=ListNode(5)
# Node5=ListNode(6)
# Node6=ListNode(7)
# lNode1.next=lNode2
# lNode2.next=lNode3
# Node4.next=Node5
# Node5.next=Node6

lNode1=ListNode(1)
Node4=ListNode(9)
Node5=ListNode(9)
Node4.next=Node5
sol = Solution()
sol.addTwoNumbers(lNode1,Node4)

# 设计测试用例：一个数为零、一个数比另一个数长、最高位有进位、连续两位有进位等等