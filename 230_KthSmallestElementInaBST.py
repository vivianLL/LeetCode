'''
230. Kth Smallest Element in a BST
Medium

https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # #　自己写的 中序遍历
        # if not root:
        #     return None
        # inorder = []
        #
        # def inorderTree(root, inorder):
        #     if root.left:
        #         inorderTree(root.left, inorder)
        #     inorder.append(root.val)
        #     if root.right:
        #         inorderTree(root.right, inorder)
        #
        # inorderTree(root, inorder)
        # if k > len(inorder):
        #     return None
        # return inorder[k - 1]

    #     # 中序遍历到需要的位置后立即返回，而不需要遍历完整棵二叉树
    #     self.k = k
    #     self.res = None
    #     self.helper(root)
    #     return self.res
    #
    # def helper(self, root):
    #     if not root:
    #         return
    #     self.helper(root.left)
    #     self.k -= 1
    #     if self.k == 0:
    #         self.res = root.val
    #         return
    #     self.helper(root.right)

        # 递归 遍历
        p = root
        cnt = k
        stack = []
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            cnt -= 1
            if cnt == 0:
                return p.val
            p = p.right

