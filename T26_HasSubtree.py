'''
剑指offer面试题26 牛客网[编程题]树的子结构

https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88?tpId=13&tqId=11170&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
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

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val==pRoot2.val:
                result = self.DoesTree1HaveTree2(pRoot1,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left,pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesTree1HaveTree2(self,pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val!=pRoot2.val:
            return False
        return self.DoesTree1HaveTree2(pRoot1.left,pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right,pRoot2.right)

sol = Solution()
tree1 = sol.buildTree([1,2,4,5,7,8,3,6],[4,2,7,5,8,1,3,6])
# tree1 = sol.buildTree([],[])
tree2 = sol.buildTree([2,4,5],[4,2,5])
ans = sol.HasSubtree(tree1,tree2)
print(ans)

# 假设结点都为整数，如果为小数则需要用abs是否足够小来判断是否相等
# 需要两个函数，一个用来判断是不是子结构，另外一个是用来进行初始化。
# 判断是否是子结构的时候，如果当前值相等，需要进行左右值是否相等的判断；如果当前值不等，则判断Root1的左右子树是否包含Root2.