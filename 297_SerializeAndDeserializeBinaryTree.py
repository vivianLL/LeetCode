'''
297. Serialize and Deserialize Binary Tree
Hard

https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
'''
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
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

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 加null字符的前序遍历
        serlist = []
        def preorder(root):   # serlist为外部变量，不用当作参数传到preorder里
            if not root:
                serlist.append("null")
            else:
                serlist.append(root.val)
                preorder(root.left)  # 此处不用根据root.left或right是否为None判断是递归还是append("null")，因为在函数里判断了
                preorder(root.right)

            return serlist
        preorder(root)
        return serlist

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 非空（#）的第一个节点是某子树的根节点，左右子节点在该根节点后，以空节点#为分隔符
        # if data == []:
        #     return None
        # val = data.pop(0)
        # root = None         # 如果val=="null"，则该节点为None
        # if val != "null":
        #     root = TreeNode(val)
        #     root.left = self.deserialize(data)
        #     root.right = self.deserialize(data)
        # return root
        
        vals = deque(val for val in data)

        def build():
            if vals:
                val = vals.popleft()
                if val == 'null':
                    return None
                root = TreeNode(val)
                root.left = build()
                root.right = build()
                return root

        return build()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
sol = Codec()

# tree = sol.buildTree([1, 2, 4, 5, 7, 8, 3, 6], [4, 2, 7, 5, 8, 1, 3, 6])
tree = sol.buildTree([1, 2, 4, 3, 5, 6], [4,2,1,5,3,6])
# tree = sol.buildTree([],[])
ans = sol.serialize(tree)
print(ans)

# 思路：难点在反序列化，递归的条件