'''
226. Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/
Invert a binary tree.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        # 根据前序和中序递归构建左右子树 224 ms，44.50%
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            return TreeNode(preorder[0])
        else:
            tree = TreeNode(preorder[0])
            i = inorder.index(preorder[0])
            tree.left = self.buildTree(preorder[1:i+1],inorder[:i])
            tree.right = self.buildTree(preorder[i+1:],inorder[i+1:])
        return tree

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 递归 时间复杂度O(n) 空间复杂度O(n)
        # if not root:
        #     return None
        # temp = root.left           # 或者 root.left, root.right = root.right, root.left     self.invertTree(root.left)   self.invertTree(root.right)
        # root.left = self.invertTree(root.right)
        # root.right = self.invertTree(temp)
        #
        # return root

        # 迭代 LeetCode可成功但pycharm运行出错 时间复杂度O(n) 空间复杂度O(n)
        if not root:
            return None
        queue = []  # 队列
        queue.append(root)   # 加入队列
        while queue:
            current = queue.pop(0)  # 删除队列的第一个元素
            temp = current.left
            current.left = current.right
            current.right = temp
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return root


sol = Solution()
tree = sol.buildTree([1, 2, 4, 5, 7, 8, 3, 6], [4, 2, 7, 5, 8, 1, 3, 6])
ans = sol.invertTree(tree.left.left.val)
print(ans)
# <__main__.TreeNode object at 0x000001E77C967A20>