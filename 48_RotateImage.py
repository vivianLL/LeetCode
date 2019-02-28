'''
48. Rotate Image

Medium
https://leetcode.com/problems/rotate-image/
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # # 顺时针旋转相当于先转置，再左右翻转
        # n = len(matrix)
        # for i in range(n):
        #     for j in range(i,n):
        #         temp = matrix[i][j]
        #         matrix[i][j] = matrix[j][i]
        #         matrix[j][i] = temp
        # for i in range(n):
        #     for j in range(0,n//2):
        #         temp = matrix[i][j]
        #         matrix[i][j] = matrix[i][n-1-j]
        #         matrix[i][n-1-j] = temp
        # print(matrix)

        # 简单方法 或者先上下翻转，再转置
        matrix[:] = map(list, zip(*matrix[::-1]))  # 注意要matrix[:]而不能matrix，否则为map形式
        print(matrix)

sol = Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
]
ans = sol.rotate(matrix)
