'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if matrix == [] or type(matrix[0])==int:   # if not matrix or not matrix[0]: return False
            return False

        row = len(matrix)
        column = len(matrix[0])


        # # 剔除右上角查找 40 ms, faster than 92.74%
        # i=0
        # j=column-1

        # while (j>=0 and i<row):
        #     if matrix[i][j]>target:
        #         j=j-1
        #     elif matrix[i][j]<target:
        #         i=i+1
        #     else:
        #         print(i, j)
        #         return True
        # return False


        # 看作一维数组 二分法查找
        # left = 0
        # right = row*column-1
        # while left<=right:
        #     mid = left+(right-left)//2   #取整除（向下取整）
        #     if matrix[mid//column][mid%column] == target:
        #         return True
        #     if matrix[mid//column][mid%column] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return False


        # 简单写法
        L = [num for sub in matrix for num in sub]  # 二重循环 二维数组转成一维数组 等价于分行写的两个for嵌套
        return target in L



matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
# matrix = [[1]]
# matrix = []
sol = Solution()
ans = sol.searchMatrix(matrix,11)
print(ans)


# 可能的输入：[] 0 [[1]] 2
# 注意while循环两个条件同时满足，需要用and，相当于&&，而不能用&(位运算)