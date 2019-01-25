'''
343. Integer Break

https://leetcode.com/problems/integer-break/
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
'''

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0,1,2,3]
        if n == 0:  # 当长度为0时，返回0
            return 0
        if n == 1:  # 当长度为1时，返回1
            return 1
        if n == 2:  # 当长度为2时，返回2
            return 2
        if n == 3:  # 当长度为3时，返回2，虽然最优解数组里为2，但是每次必须得切一刀，这样1*2=2，所以长度为3时还是2
            return 2
        for j in range(4,n+1):
            max = 0
            for i in range(1,j):
                product = ans[i]*ans[j-i]
                if product > max:
                    max = product
            ans.append(max)

        return ans[n]


sol = Solution()
ans = sol.integerBreak(8)
print(ans)

# 动态规划 or 贪婪算法
# 注意：如何将上次所得最优解追加在列表里，n=0,1,2,3时解数组和返回值的区别