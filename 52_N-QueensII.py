'''
52. N-Queens II
Hard

https://leetcode.com/problems/n-queens-ii/
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
'''
class Solution:
    # # 最慢写法 回溯法 深度优先搜索
    # def totalNQueens(self, n: int) -> int:
    #     result = []
    #     dp = [["." for _ in range(n)] for _ in range(n)]
    #     for i in range(n):
    #         dp[i][0] = "Q"
    #         self.helper(dp,result,1,n)
    #         dp[i][0] = "."
    #     return result
    #
    # def helper(self,matrix,result,column,n):
    #     if column == n:
    #         mat = []
    #         for k in range(len(matrix)):
    #             mat.append("".join(matrix[k]))
    #         print(mat)
    #         result.append(mat)
    #     else:
    #         for i in range(n):
    #             if self.isOK(matrix,i,column):
    #                 matrix[i][column] = "Q"
    #                 self.helper(matrix,result,column+1,n)
    #                 matrix[i][column] = "."
    #
    # def isOK(self,matrix,x,y):
    #     for i in range(len(matrix)):
    #         for j in range(y):
    #             if matrix[i][j] == "Q" and (i==x or j==y or (i-j)==(x-y) or (i+j)==(x+y)):
    #                 return False
    #     return True

    # # 较慢写法 给列和正反对角线编号，标记是否冲突
    # def totalNQueens(self, n: int) -> int:
    #     self.col = [False] * n        # 每一竖是否被占用
    #     self.diag = [False] * (2 * n)      # 每一对角线是否被占用
    #     self.anti_diag = [False] * (2 * n) # 每一反对角线是否被占用
    #     self.result = 0
    #     self.recursive(0, n, [])
    #     return self.result
    #
    # def recursive(self, row, n, column):
    #     if row == n:
    #         self.result += 1
    #     else:
    #         for i in range(n):
    #             if not self.col[i] and not self.diag[row + i] and not self.anti_diag[n - i + row]:
    #                 self.col[i] = self.diag[row + i] = self.anti_diag[n - i + row] = True
    #                 self.recursive(row + 1, n, column + [i])
    #                 self.col[i] = self.diag[row + i] = self.anti_diag[n - i + row] = False

    # # 更快写法
    # def totalNQueens(self, n: int) -> int:
    #     self.count = 0
    #
    #     def DFS(n, row, cols, pie, na):
    #         bits = (~(cols | pie | na)) & ((1 << n) - 1)  # 可以放置皇后的位置，对按列冲突、按左右斜对角线冲突的位置取反
    #         while bits:
    #             p = bits & -bits       # 取出可以放置皇后的位置中最右边的一个1
    #             if row == n - 1:
    #                 self.count += 1
    #             else:
    #                 DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)  # 下一行中列、左斜对角线、右斜对角线冲突的情况
    #             bits = bits & (bits - 1)
    #     DFS(n, 0, 0, 0, 0)
    #     return self.count

    def totalNQueens(self, n: int) -> int:
        global count,sol
        count = 0
        sol = [0]*n
        self.DFS(0,n)
        return count

    def DFS(self,row,n):
        global count
        for col in range(n):  # 依次试探每一列
            # 检查冲突
            ok = True
            for i in range(row):
                if col == sol[i] or col - sol[i] == row - i or col - sol[i] == i - row:
                    ok = False
                    break
            if not ok:
                continue
            # 检查冲突结束
            if row == n - 1:  # 已放到最后一行
                print(sol)
                count += 1  # 找到一组解
            else:
                sol[row] = col  # 记录当前行皇后的位置

                self.DFS(row + 1,n)

solution = Solution()
print(solution.totalNQueens(4))
