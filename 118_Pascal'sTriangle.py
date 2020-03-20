'''
118. Pascal's Triangle
Easy

https://leetcode.com/problems/pascals-triangle/
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
'''
class Solution:
    def generate(self, numRows: int):
        # if numRows==0:
        #     return []
        # elif numRows==1:
        #     return [[1]]
        # else:
        #     ans = [[1],[1,1]]
        #     for i in range(1,numRows-1):
        #         last = ans[-1]
        #         temp = [1]
        #         for j in range(len(last)-1):
        #             temp.append(last[j]+last[j+1])
        #         temp.append(1)
        #         ans.append(temp)
        # return ans

        # 官方写法
        triangle = []

        for row_num in range(numRows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

sol = Solution()
ans = sol.generate(3)
print(ans)