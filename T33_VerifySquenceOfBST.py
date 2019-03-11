'''
剑指offer面试题33 牛客网[编程题]二叉搜索树的后序遍历序列
链接：https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd?tpId=13&tqId=11176&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence==[]:
            return False
        root = sequence[-1]

        for i in range(len(sequence)):  # 应为len(sequence)而非len(sequence)-1，防止越界而导致i没有赋值而下面调用报错
            if sequence[i]>root:
                splitindex = i
                break
        for j in range(i,len(sequence)):
            if sequence[j]<root:
                return False
        # print(sequence[0:i])
        # print(sequence[i:-1])
        left = True
        right = True
        if i>0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        if i<len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])

        return left and right


sol = Solution()
sequence = [5,7,6,9,11,10,8]
ans = sol.VerifySquenceOfBST(sequence)
print(ans)