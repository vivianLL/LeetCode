'''
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.
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
    # def buildTree(self, preorder, inorder):
    #     """
    #     :type preorder: List[int]
    #     :type inorder: List[int]
    #     :rtype: TreeNode
    #     """
    #     # 递归构建左右子树 224 ms，44.50%
    #     if len(preorder)==0:
    #         return None
    #     if len(preorder)==1:
    #         return TreeNode(preorder[0])
    #     else:
    #         tree = TreeNode(preorder[0])
    #         i = inorder.index(preorder[0])
    #         tree.left = self.buildTree(preorder[1:i+1],inorder[:i])
    #         tree.right = self.buildTree(preorder[i+1:],inorder[i+1:])
    #     return tree

    # 56ms 97% 不使用数组切片，而是传递数组索引；不传数组指针，只存为类变量；预先计算中序数组的索引值
        def __init__(self):
            self.val_to_inorder_index = {}
            self.preorder = None

        def buildTree_recur(self, pre_min, pre_max, in_min):  # indices, inclusive
            if pre_max < pre_min:
                return None

            root_val = self.preorder[pre_min]
            root = TreeNode(root_val)

            if pre_max == pre_min:
                return root

            # Find out which elements belong on the left vs right sides of root.
            split_in = self.val_to_inorder_index[root_val]
            split_pre = pre_min + (split_in - in_min)  # sublist will be same length.

            # Build the left and right subtrees.
            root.left = self.buildTree_recur(pre_min + 1, split_pre, in_min)
            root.right = self.buildTree_recur(split_pre + 1, pre_max, split_in + 1)

            return root

        def buildTree(self, preorder, inorder):
            """
            :type preorder: List[int]
            :type inorder: List[int]
            :rtype: TreeNode
            """
            if not preorder or not inorder:
                return None

            self.preorder = preorder

            # preindex inorder values for quick lookup
            self.val_to_inorder_index = {val: i for i, val in enumerate(inorder)}

            return self.buildTree_recur(0, len(preorder) - 1, 0)


# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
preorder = [1,2,4,7,3,5,6,8]
inorder = [4,7,2,1,5,3,8,6]

sol = Solution()
sol.buildTree(preorder,inorder)