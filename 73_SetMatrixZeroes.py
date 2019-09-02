'''
73. Set Matrix Zeroes
Medium

https://leetcode.com/problems/set-matrix-zeroes/
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
'''
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # 时间复杂度O(mn) 空间复杂度O(m+n)
        # # 用两个集合来记录原始矩阵中0元素的行和列
        # R = len(matrix)
        # C = len(matrix[0])
        # rows, cols = set(), set()
        #
        # for i in range(R):
        #     for j in range(C):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        #
        # # 再次遍历数组并使用rows和cols集合来更新元素
        # for i in range(R):
        #     for j in range(C):
        #         if i in rows or j in cols:   # 用or来获取0所在的行和列
        #             matrix[i][j] = 0
        # print(matrix)

        # # 时间复杂度O(mn*（m+n)) 空间复杂度O(1)
        # MODIFIED = -1000000
        # R = len(matrix)
        # C = len(matrix[0])
        # for r in range(R):
        #     for c in range(C):
        #         if matrix[r][c] == 0:   # 注意：只把非零元素的位置更新为MODIFIED，原本就是0的不变
        #             for k in range(C):
        #                 matrix[r][k] = MODIFIED if matrix[r][k] != 0 else 0
        #             for k in range(R):
        #                 matrix[k][c] = MODIFIED if matrix[k][c] != 0 else 0
        # for r in range(R):              # 遍历两次，第二次再把MODIFIED变为0
        #     for c in range(C):
        #         if matrix[r][c] == MODIFIED:
        #             matrix[r][c] = 0
        # print(matrix)


        # 去除上一种方法中的冗余（每一行每一列重复判断） 用原数组的第一行第一列来记录各行各列是否有0. 因为第一行和第一列共享matrix[0][0]，所以用[0][0]代表第一行，增加一个附加变量is_col代表第一列
        # 时间复杂度O(mn) 空间复杂度O(1)
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # 再次遍历数组，并使用第一行和第一列更新元素。
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # 通过matrix[0][0]看第一行是否也需要设置为零
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # 通过is_col看第一列是否也需要设置为零
        if is_col:
            for i in range(R):
                matrix[i][0] = 0


sol = Solution()
matrix = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
sol.setZeroes(matrix)
