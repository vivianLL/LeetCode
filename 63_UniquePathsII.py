'''
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # martix = [[0 for a in range(n)] for b in range(m)]
        martix = [[0] * n] * m

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    martix[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        martix[i][j] = 1
                    elif i == 0:
                        martix[i][j] = martix[i][j - 1]
                    elif j == 0:
                        martix[i][j] = martix[i - 1][j]
                    else:
                        martix[i][j] = martix[i - 1][j] + martix[i][j - 1]
        return martix[m - 1][n - 1]

        # m = len(obstacleGrid)
        # n = len(obstacleGrid[0])
        # if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
        #     return 0
        # f = [0] * n
        # f[0] = 0 if obstacleGrid[0][0] else 1
        # for i in range(m):
        #     f[0] = 0 if f[0] == 0 else (0 if obstacleGrid[i][0] else 1)
        #     for j in range(1, n):
        #         f[j] = 0 if obstacleGrid[i][j] else f[j] + f[j - 1]
        #
        # return f[n - 1]

sol = Solution()
ans = sol.uniquePathsWithObstacles([
  [0,0,0,0],
  [0,1,0,0],
  [0,0,0,0]
])
print(ans)
ans = sol.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])
print(ans)
ans = sol.uniquePathsWithObstacles([[0]])
print(ans)
ans = sol.uniquePathsWithObstacles([[1,1]])
print(ans)
ans = sol.uniquePathsWithObstacles([[0,0],[0,1]])
print(ans)
ans = sol.uniquePathsWithObstacles([[1,0],[0,0]])
print(ans)
ans = sol.uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
print(ans)
ans = sol.uniquePathsWithObstacles([[0],[1]])
print(ans)

# 思路：与62题类似，若有障碍物，即obstacleGrid[i][j]=1，则该处可能的路径有0条，即martix[i][j] = 0；再将没有障碍物的块分成起点处[0][0]，i=0,j=0和其他，以免martix[i - 1][j]和martix[i][j - 1]越界变为负数。（如果越界不报错但结果不对）