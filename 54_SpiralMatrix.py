'''
54. Spiral Matrix
Medium

https://leetcode.com/problems/spiral-matrix/
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # # 递归 每次打印并删除矩阵的第一行，然后将矩阵逆时针翻转90度，直至打印出全部结果
        # return list(matrix[0]) + self.spiralOrder(zip(*matrix[1:])[::-1]) if matrix else []

        # 迭代 每次打印并删除矩阵的第一行，然后将矩阵逆时针翻转90度，直至打印出全部结果
        # python2可以python3不行，它不再返回一个列表而是返回一个迭代值，如果你希望输出一个列表而不是迭代值，只需要list(zip(a1,a2))
        a = []
        while matrix:
            a.extend(list(matrix.pop(0)))
            matrix = list(zip(*matrix))   # 相当于矩阵转置
            matrix.reverse()  # 对列表的元素进行反向排序。转置+左右对称=顺时针90°旋转
        return a

    #     # 每次打印并删除矩阵的第一行，然后将矩阵逆时针翻转90度，直至打印出全部结果，不使用zip和reverse
    #     result = []
    #     while matrix:                 # 防止越界
    #         result += matrix.pop(0)   # 删除第一行
    #         if matrix:
    #             matrix = self.rotate(matrix)
    #     return result
    #
    # def rotate(self, matrix):
    #     # 逆时针旋转矩阵
    #     row = len(matrix)
    #     col = len(matrix[0])
    #     # 存放旋转后的矩阵
    #     new_matrix = []
    #     # 行列调换
    #     for i in range(col):
    #         new_line = []
    #         for j in range(row):
    #             new_line.append(matrix[j][col - 1 - i])
    #         new_matrix.append(new_line)
    #     return new_matrix

        # # 按照顺时针从外到内打印，直接pop，不旋转
        # res = []
        # while matrix:
        #     res += matrix.pop(0)           # 第一行
        #     if matrix and matrix[0]:
        #         for row in matrix:
        #             res.append(row.pop())  # 每一行的最后一个，即最后一列
        #     if matrix:
        #         res += matrix.pop()[::-1]  # 从右往左的最后一行
        #     if matrix and matrix[0]:
        #         for row in matrix[::-1]:   # matrix[::-1]即从下往上排列
        #             res.append(row.pop(0)) # 从下往上排的第一个，即倒序的第一列
        # return res

        # 还有两个LeetCode官方解答，详见LeetCode


sol = Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
]
# matrix = [
#     [1, 2, 3, 4],
# ]
# matrix = [
#     [1],
#     [2],
#     [3]
# ]
# matrix = [
#     [1]
# ]
ans = sol.spiralOrder(matrix)
print(ans)
# 思路：分成两步：第一步把矩阵从外到内分为若干圈，第二步打印外圈矩阵。
# 打印最外圈的函数需要将m和n作为参数输入，否则每次调用该函数的时候需要新建一个去除最外圈的新矩阵。