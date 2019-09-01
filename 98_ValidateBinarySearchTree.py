'''
98. Validate Binary Search Tree
Medium

https://leetcode.com/problems/validate-binary-search-tree/
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # # 中序遍历
        # ans = []
        # def help(ans,root):
        #     if root:
        #         help(ans,root.left)
        #         ans.append(root.val)
        #         help(ans,root.right)
        # help(ans,root)
        # for i in range(1,len(ans)):   # 后一个必须比前一个大，不能用ans==sorted(ans)来判断
        #     if ans[i]<=ans[i-1]:
        #         return False
        # return True

        # # 递归 空间复杂度O(1)
        # def helper(node, lower=float('-inf'), upper=float('inf')):
        #     if not node:
        #         return True
        #
        #     val = node.val
        #     if val <= lower or val >= upper:
        #         return False
        #
        #     if not helper(node.right, val, upper):
        #         return False
        #     if not helper(node.left, lower, val):
        #         return False
        #     return True
        #
        # return helper(root)

        # 循环 空间复杂度O(1)
        if not root:
            return True

        stack = [(root, float('-inf'), float('inf')), ]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True