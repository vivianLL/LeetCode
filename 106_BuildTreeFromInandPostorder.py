'''
106. Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given inorder and postorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        # 递归构建左右子树 224 ms,48.43%
        if len(inorder)==0:
            return None
        if len(inorder)==1:
            return TreeNode(inorder[0])
        else:
            tree = TreeNode(postorder[-1])
            i = inorder.index(postorder[-1])
            if i == 0:  # 因为有i-1，所以需考虑往下越界i-1<0
                tree.left = None
            else:
                tree.left = self.buildTree(inorder[0:i],postorder[0:i])   # 注意：从第0个到第i-1个，为[0:i]而非[0:i-1]
            tree.right = self.buildTree(inorder[i+1:], postorder[i:-1])  # 注意：到倒数第二个是[i:-1]而非[i:-2]！
        return tree

inorder = [4,7,2,1,5,3,8,6]
postorder = [7,4,2,5,8,6,3,1]

sol = Solution()
sol.buildTree(inorder,postorder)

# 测试用例：[1,2,3,4]和[3,2,4,1]、[1,3,2]和[3,2,1]、[1,2,3,4]和[2,3,1,4]
