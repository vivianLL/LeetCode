'''
221. Maximal Square
Medium

https://leetcode.com/problems/maximal-square/
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
'''
class Solution:
    def maximalSquare(self, matrix) -> int:
        # # 暴力法 Time complexity : O((mn)**2) Space complexity : O(1)
        # if matrix==[]:
        #     return 0
        # max = 0
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):   # 注意len(matrix)和len(matrix[0])的顺序
        #         print(i,j)
        #         if matrix[i][j]=="1":
        #             n=1
        #             flag = True
        #             while i<len(matrix)-n and j<len(matrix[0])-n and flag:
        #                 for k in range(j,n+j+1):
        #                     if matrix[i+n][k]=="0":
        #                         flag = False
        #                         break
        #                 for k in range(i,n+i+1):
        #                     if matrix[k][j+n]=="0":
        #                         flag = False
        #                         break
        #                 if flag:
        #                     n+=1
        #             if n**2>max:
        #                 max = n**2
        #                 print(max)
        # return max


        # 动态规划 Time complexity : O(mn)O(mn) Space complexity : O(mn)O(mn)
        if matrix==[]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # dp应为int而非str,一定要写成for _ in range(m)的形式，如果写成dp = [[0]*n]*m，则每行统一变
        for i in range(m):                           # 单独把最左边和最上边的值列出来
            dp[i][0] = 0 if matrix[i][0]=="0" else 1
        for j in range(n):
            dp[0][j] = 0 if matrix[0][j]=="0" else 1

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=="1":
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
        return max(max(k) for k in dp)**2  # 因为最左最上边单列了，所以不能在（1,m)(1,n)的循环里求最大的正方形长度，而应对全部dp求

        # # 更快的动态规划 Time complexity : O(mn) Space complexity : O(n)
        # m = len(matrix)
        # if m == 0:
        #     return 0
        # n = len(matrix[0])
        # dp = [0] * n
        # mS = 0
        # prev = 0
        # for i in range(m):
        #     for j in range(n):
        #         tmp = dp[j]
        #         if matrix[i][j] == '1':
        #             if j == 0:
        #                 dp[j] = 1     # 防止j-1越界
        #             else:
        #                 dp[j] = min(dp[j], dp[j - 1], prev) + 1    # prev为左斜上方元素，dp为一维数组而非二维
        #         else:
        #             dp[j] = 0
        #         prev = tmp
        #         if dp[j] * dp[j] > mS:
        #             mS = dp[j] * dp[j]
        # return mS


sol = Solution()
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","1","1","1"]]
ans = sol.maximalSquare(matrix)
print(ans)
matrix = [["0","0","0","1"],
          ["1","1","0","1"],
          ["1","1","1","1"],
          ["0","1","1","1"],
          ["0","1","1","1"]]
ans = sol.maximalSquare(matrix)
print(ans)
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
ans = sol.maximalSquare(matrix)
print(ans)
matrix = [["1"]]
ans = sol.maximalSquare(matrix)
print(ans)

# 注意：暴力法不可以从左上角出发仅考虑下、右和右下，防止出现下面的情况
# [["1","1","0","0"],
#  ["1","1","1","0"],
#  ["0","1","1","0"]]
# 应检查行和列的所有元素是否为1（设置flag判断）
# 动态规划法 以矩阵中每一个点作为正方形右下角点来处理，而以该点为右下角点的最大边长最多比以它的左方、上方和左上方为右下角的正方形边长多1，所以这时只能取另外三个正方形中最小的正方形边长+1。用d[i][j]表示以i，j坐标为右下角的正方形最大边。
# 则有状态转移方程：dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
