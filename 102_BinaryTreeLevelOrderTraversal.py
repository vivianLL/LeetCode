'''
102. Binary Tree Level Order Traversal
Medium

https://leetcode.com/problems/binary-tree-level-order-traversal/
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        output = []

        if root is None:
            return output

        stack = []
        stack.append(root)

        while (stack):
            curr_level = []
            next_level = []

            for node in stack:
                curr_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            stack = next_level
            output.append(curr_level)

        return output
        # # 按剑指offer直接打印一维列表 单个保存节点到队列
        # if not root:
        #     return None
        # queue = []
        # queue.append(root)
        # traversal = []
        # layer = []
        # while len(queue):
        #     node = queue.pop(0)
        #     layer.append(node.val)
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        # traversal.append(layer)
        # return traversal

        # 按层打印二维数组
        res = []
        self.preorder(res, 0, root)
        return res

    def preorder(self, res, level, root):
        if root:
            if len(res) < level + 1:
                res.append([])

            res[level].append(root.val)

            self.preorder(res, level + 1, root.left)
            self.preorder(res, level + 1, root.right)


# 1、先序遍历
# 2、每次记录层次，作为子数组的index
# 3、将每次的root节点append到指定层次的子数组中

