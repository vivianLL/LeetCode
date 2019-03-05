'''
103. Binary Tree Zigzag Level Order Traversal
Medium

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
For example:
Given binary tree [3,9,20,null,null,15,7],return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode):
        # if not root:
        #     return []
        # output = []
        # stack = []
        # stack.append(root)
        # n = 0
        # while stack:
        #     n = n + 1
        #     curr_level = []
        #     next_level = []
        #     for node in stack:
        #         curr_level.append(node.val)
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
        #
        #     stack = next_level
        #     if n % 2 == 1:
        #         output.append(curr_level)
        #     else:
        #         output.append(curr_level[::-1])
        # return output

        q = [(root, 1)]
        ret = []
        if root == None:
            return ret

        while len(q) > 0:
            n, l = q.pop(0)
            if len(ret) < l:
                ret.append([])

            ret[l - 1].append(n.val)

            if n.right != None:
                q.append((n.right, l + 1))
            if n.left != None:
                q.append((n.left, l + 1))

        for i in range(len(ret)):  # i保存层数
            if i % 2 == 0:
                ret[i].reverse()
        return ret

# 思路：在102题的基础上将列表反向