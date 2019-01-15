# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # # 存入列表倒序打印 相当于栈结构 pop操作
        # l = []
        # while(listNode!=None):
        #     # print(listNode.val)
        #     l.append(listNode.val)
        #     listNode=listNode.next
        # # while(l!=[]):
        # #     print(l.pop())
        # return l[::-1]  # 倒序打印

        # 递归
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]  # python里面list型添加元素可以直接+[num]

lNode1 = ListNode(1)
lNode2 = ListNode(2)
lNode3 = ListNode(3)
lNode4 = ListNode(4)
lNode5 = ListNode(5)
lNode1.next = lNode2
lNode2.next = lNode3
lNode3.next = lNode4
lNode4.next = lNode5
sol = Solution()
sol.printListFromTailToHead(lNode1)
