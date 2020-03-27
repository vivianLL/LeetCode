'''
892. Surface Area of 3D Shapes
Easy

https://leetcode.com/problems/surface-area-of-3d-shapes/
On a N * N grid, we place some 1 * 1 * 1 cubes.
Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
Return the total surface area of the resulting shapes.
'''
class Solution:
    def surfaceArea(self, grid) -> int:
        # # 我的方法
        # if grid==[[]]:
        #     return 0
        # n = len(grid)
        # m = len(grid[0])
        # sumArea = 0   # 总表面积*6-重叠部分面积：每个块的高度(i-1)*2
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j]>1:
        #             sumArea += grid[i][j]*6 - (grid[i][j]-1)*2
        #         else:
        #             sumArea += grid[i][j]*6
        # # print(sumArea)
        # for i in range(n):
        #     for j in range(m):
        #         if j>0:
        #             sumArea -= 2*min(grid[i][j],grid[i][j-1])
        #         if i>0:
        #             sumArea -= 2*min(grid[i][j],grid[i-1][j])
        # return sumArea

        # 我的方法 两个for循环合二为一
        if grid==[[]]:
            return 0
        n = len(grid)
        m = len(grid[0])
        sumArea = 0   # 总表面积*6-重叠部分面积：每个块的高度(i-1)*2
        for i in range(n):
            for j in range(m):
                if grid[i][j]>1:
                    sumArea += grid[i][j]*6 - (grid[i][j]-1)*2
                else:
                    sumArea += grid[i][j]*6
                if j>0:
                    sumArea -= 2*min(grid[i][j],grid[i][j-1])
                if i>0:
                    sumArea -= 2*min(grid[i][j],grid[i-1][j])
        return sumArea

sol = Solution()
ans = sol.surfaceArea([[1,2],[3,4]])
print(ans)
sol = Solution()
ans = sol.surfaceArea([[1,0],[0,2]])
print(ans)
sol = Solution()
ans = sol.surfaceArea([[1,1,1],[1,0,1],[1,1,1]])
print(ans)
sol = Solution()
ans = sol.surfaceArea([[2,2,2],[2,1,2],[2,2,2]])
print(ans)