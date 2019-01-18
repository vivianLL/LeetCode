'''
62. Unique Paths
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
'''
import math

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 组合法
        return math.factorial(m + n - 2) // math.factorial(m - 1) // math.factorial(n - 1)  # factorial阶乘

        # 动态规划 时间复杂度O(mn)
        martix = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    martix[i][j] = 1
                else:
                    martix[i][j] = martix[i - 1][j] + martix[i][j - 1]   # 与martix[i + 1][j] + martix[i][j + 1]实际上一样
        print(martix)
        return martix[m - 1][n - 1]  # 左上角元素 注意是[m - 1][n - 1]而不是[m][n]


sol = Solution()
ans = sol.uniquePaths(3,2)
print(ans)
ans = sol.uniquePaths(7,3)
print(ans)

# 思路：
# 动态规划 状态转移方程，martix[i][j] = martix[i - 1][j] + martix[i][j - 1],即走完m，n个格子总的走法相当于其右方和下方的所需步数的和。
# 组合法 数学模型，其实就是机器人总共走m+n-2步，其中m-1步往下走，n-1步往右走，本质上就是一个组合问题，也就是从m+n-2个不同元素中每次取出m-1个元素的组合数。根据组合的计算公式