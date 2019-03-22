'''
110. Balanced Binary Tree
Easy

https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root) -> bool:
        # # 遍历树的每个节点时，调用深度函数得到左右子树的深度（大量重复）
        # def maxDepth(root: TreeNode) -> int:
        #     if not root: return 0
        #     nleft = maxDepth(root.left)
        #     nright = maxDepth(root.right)
        #
        #     return nleft + 1 if nleft > nright else nright + 1
        #
        # if not root: return True    # 没有根节点时是平衡的
        # if abs(maxDepth(root.right) - maxDepth(root.left)) > 1:
        #     return False
        # else:
        #     return self.isBalanced(root.left) and self.isBalanced(root.right)
        #     # 注意最后不能仅返回True，而要继续对左右子树是否平衡进行判断


        # 从下到上（从底到顶），分别判断某节点的左右子树是否为平衡二叉树，即根据该结点的左右子树高度差判断是否平衡。
        def dfs(node):
            if not node:
                return 1
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            if not left_depth or not right_depth:  # 左右两子树有一个返回False，则此处即返回False，若左右两子树都有深度且差<=1，则返回True
                return False
            if abs(left_depth - right_depth) > 1:
                return False
            return max(left_depth, right_depth) + 1

        if not root:
            return True
        if not dfs(root):   # 若dfs里返回False，则此处也返回False
            return False
        return True