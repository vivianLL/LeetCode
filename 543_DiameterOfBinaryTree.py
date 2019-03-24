'''
543. Diameter of Binary Tree
Easy

https://leetcode.com/problems/diameter-of-binary-tree/
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1       # 最长的路径上包含的节点数 相当于全局变量
        def depth(node):   # 计算深度
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)    # 在前面计算L、R时对depth的调用里已经更新了self.ans的值，使之是左右子树直径节点数中的最大值
            return max(L, R) + 1

        depth(root)
        return self.ans - 1   # 直径等于节点数减1

# 思路：
# 二叉树的直径：二叉树中从一个结点到另一个节点最长的路径，叫做二叉树的直径
# 采用分治和递归的思想：根节点为root的二叉树的直径上的节点数 = max(root.left的直径节点数，root.right的直径节点数，root.left的最大深度+root.right的最大深度+1)
root = TreeNode(2)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)
root.right = TreeNode(8)
root.left.right = TreeNode(6)
root.left.right.right = TreeNode(7)
sol = Solution()
sol.diameterOfBinaryTree(root)
