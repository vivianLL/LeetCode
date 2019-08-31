'''
22. Generate Parentheses
Medium

https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution:
    def generateParenthesis(self, n: int):
        # # 暴力法 递归生成全部2^(2n)个左括号和右括号的序列，检查是否有效
        # # 时间和空军复杂度O(n*2^(2n))
        # def generate(A=[]):
        #     print(A, ans)
        #     if len(A) == 2 * n:
        #         if valid(A):
        #             ans.append("".join(A))
        #     else:
        #         A.append('(')
        #         generate(A)
        #         A.pop()
        #         A.append(')')
        #         generate(A)
        #         A.pop()
        #
        # def valid(A):
        #     bal = 0
        #     for c in A:
        #         if c == '(':
        #             bal += 1
        #         else:
        #             bal -= 1
        #         if bal < 0: return False
        #     return bal == 0
        #
        # ans = []
        # generate()
        # return ans

        # 回溯法 时间空间复杂度O(4^n/n*sqrt(n))
        ans = []
        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans

        # 闭包  时间空间复杂度O(4^n/n*sqrt(n)) 为了枚举某些内容，我们通常希望将其表示为更容易计算的不相交子集的总和。
        # 考虑有效括号序列 S 的闭包数：至少存在index> = 0，使得 S[0], S[1], …, S[2*index+1]是有效的。 显然，每个括号序列都有一个唯一的闭包号。 我们可以尝试单独列举它们。
        # (本质还是递归，把n的括号生成分解为0和n-1的组合，1和n-2的组合，...，n-1和0的组合，依然是卡特兰数的思想)
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n - 1 - c):
                    ans.append('({}){}'.format(left, right))
                    print(left,right,ans)
        return ans



sol = Solution()
ans = sol.generateParenthesis(2)
print(ans)

# 思路：假设S(n)为n对括号的正确配对数目，那么有递推关系S(n)=S(0)S(n-1)+S(1)S(n-2) +...+S(n-1)S(0)，显然S(n)是卡特兰数。