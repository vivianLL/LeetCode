'''
236. 二叉树的最近公共祖先

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
中等
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def __init__(self):
            # Variable to store LCA node.
            self.ans = None

        def lowestCommonAncestor(self, root, p, q):
            # # 法一 递归 时间空间复杂度O(N)
            # def recurse_tree(current_node):
            #
            #     # If reached the end of a branch, return False.
            #     if not current_node:
            #         return False
            #
            #     # Left Recursion
            #     left = recurse_tree(current_node.left)
            #
            #     # Right Recursion
            #     right = recurse_tree(current_node.right)
            #
            #     # If the current node is one of p or q
            #     mid = current_node == p or current_node == q
            #
            #     # If any two of the three flags left, right or mid become True.
            #     if mid + left + right >= 2:
            #         self.ans = current_node   # 注意这个不应是返回值
            #
            #     # Return True if either of the three bool values is True.
            #     return mid or left or right
            #
            # # Traverse the tree
            # recurse_tree(root)
            # return self.ans

            # 使用父指针迭代 时间空间复杂度O(N)
            # Stack for tree traversal
            stack = [root]

            # Dictionary for parent pointers
            parent = {root: None}

            # Iterate until we find both the nodes p and q
            while p not in parent or q not in parent:

                node = stack.pop()

                # While traversing the tree, keep saving the parent pointers.
                if node.left:
                    parent[node.left] = node
                    stack.append(node.left)
                if node.right:
                    parent[node.right] = node
                    stack.append(node.right)

            # Ancestors set() for node p.
            ancestors = set()

            # Process all ancestors for node p using parent pointers.
            while p:
                ancestors.add(p)
                p = parent[p]

            # The first ancestor of q which appears in
            # p's ancestor set() is their lowest common ancestor.
            while q not in ancestors:
                q = parent[q]
            return q

            # 无父指针迭代 时间空间复杂度O(N) 略复杂 详见LeetCode

# 思路：
# 递归
# 从根节点开始遍历树。
# 如果当前节点本身是 p 或 q 中的一个，我们会将变量 mid 标记为 true，并继续搜索左右分支中的另一个节点。
# 如果左分支或右分支中的任何一个返回 true，则表示在下面找到了两个节点中的一个。
# 如果在遍历的任何点上，左、右或中三个标志中的任意两个变为 true，这意味着我们找到了节点 p 和 q 的最近公共祖先。

# 使用父指针迭代
# 从根节点开始遍历树。
# 在找到 p 和 q 之前，将父指针存储在字典中。
# 一旦我们找到了 p 和 q，我们就可以使用父亲字典获得 p 的所有祖先，并添加到一个称为祖先的集合中。
# 同样，我们遍历节点 q 的祖先。如果祖先存在于为 p 设置的祖先中，这意味着这是 p 和 q 之间的第一个共同祖先（同时向上遍历），因此这是 LCA 节点。