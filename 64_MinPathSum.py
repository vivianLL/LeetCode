'''
64. Minimum Path Sum
Medium

https://leetcode.com/problems/minimum-path-sum/
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
'''
class Solution:
    def minPathSum(self, grid) -> int:
        # # 辅助二维数组
        # if grid==[] or grid==[[]]:return 0
        # m = len(grid)
        # n = len(grid[0])
        # print(m,n)
        # dp = [[0 for i in range(n)] for j in range(m)]   # 注意m,n的顺序！再次注意 不要test = [[0] * m] * n
        #
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 and j==0:
        #             dp[i][j] = grid[i][j]
        #         elif j==0:
        #             up = dp[i-1][j]
        #             dp[i][j] = up + grid[i][j]
        #         elif i==0:
        #             left = dp[i][j-1]
        #             print(i,j)
        #             dp[i][j] = left + grid[i][j]
        #         else:
        #             up = dp[i - 1][j]
        #             left = dp[i][j - 1]
        #             dp[i][j]=min(left,up) + grid[i][j]
        # print(dp)
        # maxvalue = dp[m-1][n-1]
        # return maxvalue

        # 辅助一维数组


        # # 不用辅助数组 直接在原矩阵上改
        n = len(grid)
        m = len(grid[0])
        for i in range(1, n):
            grid[i][0] = grid[i - 1][0] + grid[i][0]  # 首先需要寻找左边界各点的路径总和

        for j in range(1, m):
            grid[0][j] = grid[0][j - 1] + grid[0][j]  # 寻找上边界各点的路径总和

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]  # 以边界处为依据一步步推出内部个点的路径总和

        return grid[n - 1][m - 1]

sol = Solution()
# grid = [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]          # 7
# grid = [[1,2,5],[3,2,1]]
grid = [[1,2],[5,6],[1,1]]
maxvalue = sol.minPathSum(grid)
print(maxvalue)
