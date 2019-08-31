'''
240. Search a 2D Matrix II
Medium

https://leetcode.com/problems/search-a-2d-matrix-ii/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:return False
        n = len(matrix[0])
        m = len(matrix)

        i = n-1
        j = 0
        while i>=0 and j<m:
            if target == matrix[j][i]:
                return True
            elif target < matrix[j][i]:
                i = i-1
            else:
                j += 1
        return False

sol = Solution()
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
# matrix = [[1,1]]
matrix = [[]]
target = 5
ans = sol.searchMatrix(matrix,target)
print(ans)