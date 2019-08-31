'''
94. Binary Tree Inorder Traversal
Medium

https://leetcode.com/problems/binary-tree-inorder-traversal/
Given a binary tree, return the inorder traversal of its nodes' values.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode):
        # 递归
        # ans = []
        # def help(ans,root):
        #     if root:
        #         help(ans,root.left)
        #         ans.append(root.val)
        #         help(ans,root.right)
        # help(ans,root)
        # return ans

        # # 非递归
        # stack = []
        # res = []
        # if not root:
        #     return []
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     if stack:
        #         a = stack.pop()
        #         root = a.right
        #         res.append(a.val)
        # return res

        # 非递归另一种写法 先把根节点入栈，如果左子树一直不为空，就一直入栈，直到把所有左节点入栈，然后pop栈顶元素，指针指向栈顶元素的右子树
        ans = []
        stack = []
        pos = root
        while pos or len(stack)>0:
            if pos:
                stack.append(pos)
                pos = pos.left
            else:
                pos = stack.pop()
                ans.append(pos.val)
                pos = pos.right
        return ans

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

sol = Solution()
ans = sol.inorderTraversal(root)
print(ans)