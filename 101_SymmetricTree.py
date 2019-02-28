'''
101. Symmetric Tree

https://leetcode.com/problems/symmetric-tree/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric,But the following [1,2,2,null,3,null,3] is not.
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

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # # 自己写的通过前序和自定义后序来建立两个列表判断，迭代
        # def readTree1(list, tree):
        #     if not tree:
        #         list.append("null")  # 不能return None
        #     else:
        #         list.append(tree.val)
        #         list = readTree1(list, tree.left)  # 此两句应在else里
        #         list = readTree1(list, tree.right)
        #     return list
        #
        # def readTree2(list, tree):
        #     if not tree:
        #         list.append("null")  # 不能return None
        #     else:
        #         list.append(tree.val)
        #         list = readTree2(list, tree.right)
        #         list = readTree2(list, tree.left)  # 此两句应在else里
        #     return list
        #
        # list1 = readTree1([], root)
        # list2 = readTree2([], root)
        # print(list1, list2)
        # return list1 == list2

        # # 在100题的基础上，判断左右子树是否对称，递归
        # def isMirrorTree(p, q):
        #     if p is None and q is None:
        #         return True
        #     if p is None or q is None:
        #         return False
        #     while p and q:
        #         if p.val == q.val and isMirrorTree(p.left, q.right) and isMirrorTree(p.right, q.left):  # 注意，此处是left和right判等，和100题不同
        #             return True
        #         return False
        #
        # if not root:
        #     return True
        # else:
        #     # p=root.left;q=root.right
        #     return isSameTree(root.left, root.right)

        # 在100题和226题的基础上，判断左子树和翻转的右子树是否相等，递归（判断原树和翻转的树是否相等则不行，不知为何）
        def invertTree(root):
            if not root:
                return None
            temp = root.left
            root.left = invertTree(root.right)
            root.right = invertTree(temp)
            return root

        def isSameTree(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            while p and q:
                if p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
                    return True
                return False

        if not root:
            return True
        else:
            invert = invertTree(root.right)
            return isSameTree(root.left, invert)


sol = Solution()

# tree = sol.buildTree([1, 2, 4, 5, 7, 8, 3, 6], [4, 2, 7, 5, 8, 1, 3, 6])
tree = sol.buildTree([1, 2, 4, 5, 7, 8, 3, 6], [4, 2, 7, 5, 8, 1, 3, 6])
ans = sol.isSymmetric(tree)
print(ans)