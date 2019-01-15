# -*- coding:utf-8 -*-
'''
剑指offer面试题8 牛客网[编程题]二叉树的下一个结点
链接：https://www.nowcoder.com/questionTerminal/9023a0c988684a53960365b889ceaf5e
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None  #指向父节点的指针

class Solution:
    def GetNext(self, pNode):
        if pNode.right:
            while pNode.right !=None:
                pNode = pNode.right
        # 分类讨论
        if pNode.right:  # 有右子树
            p = pNode.right
            while p.left:
                p = p.left
            print(p.val)
            return p
        while pNode.next:  # 无右子树，则找第一个当前节点是父节点左孩子的节点
            if (pNode.next.left == pNode):
                print(pNode.next.val)
                return pNode.next
            pNode = pNode.next  # 沿着父节点向上遍历
        return  # 到了根节点仍没找到，则返回空

    #     dummy = pNode
    #     while dummy.next:
    #         dummy = dummy.next
    #     self.result = []
    #     self.midTraversal(dummy)
    #     print(self.result[self.result.index(pNode) + 1] if self.result.index(pNode) != len(
    #         self.result) - 1 else None)
    #     return self.result[self.result.index(pNode) + 1] if self.result.index(pNode) != len(
    #         self.result) - 1 else None
    #
    # def midTraversal(self, root):
    #     if not root: return
    #     self.midTraversal(root.left)
    #     self.result.append(root)
    #     self.midTraversal(root.right)

Tree1 = TreeLinkNode(1)
Tree1.left = TreeLinkNode(2)
Tree1.right = TreeLinkNode(3)
Tree1.left.next = Tree1
Tree1.right.next = Tree1

Tree1.right.left =TreeLinkNode(4)
Tree1.right.right = TreeLinkNode(5)
Tree1.right.left.next =Tree1.right
Tree1.right.right.next = Tree1.right

Tree1.right.left.left =TreeLinkNode(8)
Tree1.right.left.right = TreeLinkNode(6)
Tree1.right.left.left.next =Tree1.right.left
Tree1.right.left.right.next = Tree1.right.left

Tree1.right.right.left = TreeLinkNode(7)
Tree1.right.right.left.next = Tree1.right.right
sol = Solution
sol.GetNext(sol,Tree1.right.right.left)

'''
先写一个中序遍历的算法。关键是从根节点开始遍历，所以第一步还是找到某个节点的根节点，方法是一直使用next判断即可。
再将从根节点中序遍历的结果保存到一个数组中，直接找pNode所在索引的下一个即可。当然要考虑这个节点是不是最后一个，如果是最后一个，直接返回None。
'''
