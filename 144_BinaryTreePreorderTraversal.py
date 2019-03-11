'''
144. Binary Tree Preorder Traversal
Medium

https://leetcode.com/problems/binary-tree-preorder-traversal/
Given a binary tree, return the preorder traversal of its nodes' values.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # # 递归
        # pre = []  # 注意要把列表在函数外初始化
        #
        # def preorder(pre, root):
        #     if not root:
        #         return []
        #     pre.append(root.val)
        #     if root.left:
        #         preorder(pre, root.left)
        #     if root.right:
        #         preorder(pre, root.right)
        #     return pre
        #
        # return preorder(pre, root)

        # 非递归
        current = root
        stack = []
        ans = []

        while True:
            if current is not None:
                ans.append(current.val)
                stack.append(current.right)
                current = current.left
            elif len(stack):
                current = stack.pop()
            else:
                break

        return ans
        ## 思路：借助辅助栈。当根结点存在，保存结果，根结点入栈；将根结点指向左子树；根结点不存在，栈顶元素出栈，并将根结点指向栈顶元素的右子树；直到栈空。