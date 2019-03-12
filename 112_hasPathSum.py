'''
112. Path Sum
Easy

https://leetcode.com/problems/path-sum/
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    #     node = root
    #     return self.traverse(node, 0, sum)
    #
    # def traverse(self, node, s, sum):
    #     if node == None:
    #         return False
    #     s += node.val
    #     if node.left == None and node.right == None:
    #         return s == sum
    #     return self.traverse(node.left, s, sum) or self.traverse(node.right, s, sum)
