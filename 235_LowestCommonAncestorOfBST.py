'''
235. Lowest Common Ancestor of a Binary Search Tree
Easy

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # # 法1 递归 利用BST性质 判断两个节点是否同时在左/右子树 时间O(n) 空间O(n)
        #
        # if p.val > root.val and q.val > root.val:   # 都在右子树
        #     return self.lowestCommonAncestor(root.right, p, q)
        # # If both p and q are lesser than parent
        # elif p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # # We have found the split point, i.e. the LCA node.
        # else:
        #     return root

        # 法2 迭代 时间O(n) 空间O(1)
        while root:
            if p.val > root.val and q.val > root.val:   # 都在右子树
                root = root.right
            elif p.val < root.val and q.val < root.val:  # 都在左子树
                root = root.left
            else:
                return root
