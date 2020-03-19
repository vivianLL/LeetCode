'''
108. Convert Sorted Array to Binary Search Tree
Easy

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        # 中序遍历，始终选择中间位置左边元素作为根节点
        def helper(left, right):
            if left > right:
                return None

            p = (left + right) // 2
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)

        # # 中序遍历，始终选择中间位置右边元素作为根节点
        # def helper(left, right):
        #     if left > right:
        #         return None
        #
        #     p = (left + right) // 2
        #     if (left + right) % 2:
        #         p += 1
        #         # p += randint(0, 1)    # 选择任意一个中间位置元素作为根节点
        #
        #     root = TreeNode(nums[p])
        #     root.left = helper(left, p - 1)
        #     root.right = helper(p + 1, right)
        #     return root
        #
        # return helper(0, len(nums) - 1)



# 注意：是高度平衡的二叉树，结果不唯一
