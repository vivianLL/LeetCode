'''
145. Binary Tree Postorder Traversal
Hard

https://leetcode.com/problems/binary-tree-postorder-traversal/
Given a binary tree, return the postorder traversal of its nodes' values.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:   # 放在函数里也可以
    #         return []
    #
    #     postorder = []
    #     def Traversal(postorder, root):
    #         if root.left:
    #             Traversal(postorder, root.left)
    #         if root.right:
    #             Traversal(postorder, root.right)
    #         postorder.append(root.val)
    #
    #     Traversal(postorder, root)
    #     return postorder

    def __init__(self):
        self.answer = []

    def postorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return self.answer

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.answer.append(root.val)

        return self.answer