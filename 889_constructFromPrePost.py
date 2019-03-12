'''
889. Construct Binary Tree from Preorder and Postorder Traversal
Medium

https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
Return any binary tree that matches the given preorder and postorder traversals.
Values in the traversals pre and post are distinct positive integers.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre, post) -> TreeNode:
        # # Time Complexity: O(N^2) Space Complexity: O(N^2)
        # if not pre:
        #     return None
        # root = TreeNode(pre[0])
        # if len(pre) == 1:
        #     return root
        #
        # L = post.index(pre[1]) + 1
        # root.left = self.constructFromPrePost(pre[1:L + 1], post[:L])
        # root.right = self.constructFromPrePost(pre[L + 1:], post[L:-1])
        # return root

        # if pre==[] or post==[]:
        #     return None
        #
        # root = TreeNode(pre[0])
        # if len(pre)==1:
        #     return root
        # L = post.index(pre[1])
        # print(pre[1:L+2],post[0:L+1])
        # root.left = self.constructFromPrePost(pre[1:L+2],post[0:L+1])
        # print(pre[L+2:],post[L+1:-1])
        # root.right = self.constructFromPrePost(pre[L+2:],post[L+1:-1])
        # return root

        # Time Complexity: O(N^2) Space Complexity: O(N)
        # (i0, i1, N) refers to pre[i0:i0+N], post[i1:i1+N]
        def make(i0, i1, N):
            if N == 0:
                return None
            root = TreeNode(pre[i0])
            if N == 1:
                return root

            for L in range(N):
                if post[i1 + L - 1] == pre[i0 + 1]:
                    break

            root.left = make(i0 + 1, i1, L)
            root.right = make(i0 + L + 1, i1 + L, N - 1 - L)
            return root

        return make(0, 0, len(pre))

pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
sol = Solution()
sol.constructFromPrePost(pre,post)

# 注意：递归的返回值是什么，怎样把节点连起来，递归到什么时候停止
# 节省空间：只传数组的索引，不新建数组
