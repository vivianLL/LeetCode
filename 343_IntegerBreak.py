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
        # # 动态规划 O(n^2)时间和O(n)空间
        # ans = [0,1,2,3]
        # if n == 0:  # 当长度为0时，返回0
        #     return 0
        # if n == 1:  # 当长度为1时，返回1
        #     return 1
        # if n == 2:  # 当长度为2时，返回2
        #     return 2
        # if n == 3:  # 当长度为3时，返回2，虽然最优解数组里为2，但是每次必须得切一刀，这样1*2=2，所以长度为3时还是2
        #     return 2
        # for j in range(4,n+1):
        #     max = 0
        #     for i in range(1,j):
        #         product = ans[i]*ans[j-i]
        #         if product > max:
        #             max = product
        #     ans.append(max)
        #
        # return ans[n]

        # 贪婪法 时间复杂度与空间复杂度都是O（1）
        if n == 0:  # 当长度为0时，返回0
            return 0
        if n == 1:  # 当长度为1时，返回1
            return 1
        if n == 2:  # 当长度为2时，返回1，注意此时和动态规划法中n==2的区别
            return 1
        if n == 3:  # 当长度为3时，返回2，虽然最优解数组里为2，但是每次必须得切一刀，这样1*2=2，所以长度为3时还是2
            return 2
        if n % 3 == 1:  # 取模,返回余数
            num = n // 3 - 1  # 取商的整数部分（向下取整）
            return 3 ** (num) * 4  # 幂
        if n % 3 == 2:
            num = n // 3
            return 3 ** (num) * 2
        if n % 3 == 0:
            num = n // 3
            return 3 ** num



sol = Solution()
ans = sol.integerBreak(2)
print(ans)
ans = sol.integerBreak(4)
print(ans)


# 动态规划 or 贪婪算法
# 注意：如何将上次所得最优解追加在列表里，n=0,1,2,3时解数组和返回值的区别
# 贪婪算法思想：2不能割，3最优分割为3>1X2,4被分割最优为4=2X2，5被分割最优为2x3，6为3X3，我有一个大胆的想法，保证3的个数如果有1为余数那就减少一个3用来凑成4=2X2（保证不比割前小即可）这样问题好像还真的就得到了解决。因为2(n-2)与3（n-3）只有在5的时候是相等的，当n大于5的时候3（n-3）是最优的。
