'''
100. Same Tree
Easy

https://leetcode.com/problems/same-tree/
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # # 读到列表里再判断
        # def readTree(list, tree):
        #     if not tree:
        #         list.append("null")  # 不能return None
        #     else:
        #         list.append(tree.val)
        #         list = readTree(list, tree.left)   # 此两句应在else里
        #         list = readTree(list, tree.right)
        #     return list
        #
        # plist = readTree([], p)
        # qlist = readTree([], q)
        # print(plist, qlist)
        # return plist == qlist

        # 直接递归判断
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        while p and q:
            if p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            return False