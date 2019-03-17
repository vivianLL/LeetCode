'''
剑指offer面试题36 二叉搜索树与双向链表

https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=13&tqId=11179&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 先将BST转成列表，再从列表转成双向链表
    def Convert(self, pRootOfTree):
    #     # write code here
    #     inorder = self.ConvertToList(pRootOfTree)
    #     if inorder == []:          # 防止越界
    #         return None
    #     head = TreeNode(inorder[0])
    #     head.left = None
    #     binode = head              # 头结点
    #     for i in range(1, len(inorder)):   # 注意范围
    #         node = TreeNode(inorder[i])
    #         binode.right = node
    #         binode.right.left = binode
    #         binode = binode.right
    #     binode.next = None
    #     return head
    #
    #
    # def ConvertToList(self,pRootOfTree):
    #     if not pRootOfTree:   # 放在函数里也可以
    #         return []
    #     inorder = []
    #     def Traversal(inorder, root):
    #         if root.left:
    #             Traversal(inorder, root.left)
    #         inorder.append(root.val)
    #         if root.right:
    #             Traversal(inorder, root.right)
    #     Traversal(inorder, pRootOfTree)
    #     return inorder


    #     # 牛客网原地解法
    #     self.linkedlistLast = None    # 指向双向链表尾节点
    #     self.convertNode(pRootOfTree)
    #     pHead = self.linkedlistLast   # 需要返回头结点
    #     while pHead and pHead.left:
    #         pHead = pHead.left
    #     return pHead
    #
    # def convertNode(self, root):
    #     if not root:
    #         return
    #     pcurr = root                  # 中序遍历
    #     if pcurr.left:
    #         self.convertNode(pcurr.left)
    #     pcurr.left = self.linkedlistLast    # 最左边的节点的前节点为None
    #     if self.linkedlistLast:
    #         self.linkedlistLast.right = pcurr
    #     self.linkedlistLast = pcurr         # 头结点为最左边的节点
    #     if pcurr.right:
    #         self.convertNode(pcurr.right)

        # 牛客网递归写法
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        # 将左子树构建成双链表，返回链表头
        left = self.Convert(pRootOfTree.left)
        p = left

        # 定位至左子树的最右的一个结点
        while left and p.right:
            p = p.right

        # 如果左子树不为空，将当前root加到左子树链表
        if left:
            p.right = pRootOfTree
            pRootOfTree.left = p

        # 将右子树构造成双链表，返回链表头
        right = self.Convert(pRootOfTree.right)
        # 如果右子树不为空，将该链表追加到root结点之后
        if right:
            right.left = pRootOfTree
            pRootOfTree.right = right

        return left if left else pRootOfTree

        # 牛客网非递归
        if not pRootOfTree:
            return None

        p = pRootOfTree

        stack = []
        resStack = []

        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                resStack.append(node)
                p = node.right

        resP = resStack[0]
        while resStack:
            top = resStack.pop(0)
            if resStack:
                top.right = resStack[0]
                resStack[0].left = top

        return resP

sol = Solution()
bst = sol.buildTree([4,7,2,1,5,3,8,6],[7,4,2,5,8,6,3,1])
inorder = sol.ConvertToList(bst)
print(inorder)