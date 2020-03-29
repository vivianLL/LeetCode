'''
1162. 地图分析
Medium

https://leetcode-cn.com/problems/as-far-from-land-as-possible/
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。
'''
class Solution:
    def maxDistance(self, grid) -> int:
        # # BFS/染色 逐步膨胀
        # ans = 0
        # stage = 1  # 每陆地开始，第一个染色时stage+1，区分出陆地
        # n = len(grid)
        # for i in grid:
        #     ans += sum(i)
        # if ans == 0 or ans == n * n:  # 判断是不是全是陆地或者海洋，是的话返回-1
        #     return -1
        #
        # while (1):
        #     for i in range(n):
        #         for j in range(n):
        #             # 从每一批颜色出发，颜色逐渐扩散
        #             if grid[i][j] == stage:
        #                 for move_i, move_j in [1, 0], [-1, 0], [0, 1], [0, -1]:
        #                     if i + move_i < 0 or i + move_i > n - 1 or j + move_j < 0 or j + move_j > n - 1:
        #                         continue
        #                     if grid[i + move_i][j + move_j] > stage + 1 or grid[i + move_i][j + move_j] == 0:
        #                         grid[i + move_i][j + move_j] = stage + 1
        #     print(grid, stage)
        #     for i in grid:
        #         if 0 in i:
        #             break  # 这个break后执行stage += 1
        #     else:  # 当i中没有0时执行else
        #         print("test", i)
        #         break  # 这个break后执行return stage
        #     stage += 1
        #
        # return stage

        # 染色的简介写法 便于理解
        n = len(grid)
        steps = -1         # 由于没有early return，steps会多算一次。可以返回值减去1，也可以steps初始化为-1。
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        print(queue)
        if len(queue) == 0 or len(queue) == n ** 2: return steps  # 判断是不是全是陆地或者海洋，是的话返回-1
        while len(queue) > 0:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xi >= 0 and xi < n and yj >= 0 and yj < n and grid[xi][yj] == 0:
                        queue.append((xi, yj))
                        grid[xi][yj] = -1
            steps += 1   # 每向四个方向膨胀/染色一次，完成后steps加1

        return steps

        # # 快速方法
        # m = len(grid)
        # n = len(grid[0])
        # store = [[0 for _ in range(n)] for _ in range(m)]
        # waterCount = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 0:
        #             waterCount += 1
        #             if i == 0 and j == 0:
        #                 store[i][j] = m + n - 2
        #             elif i == 0:
        #                 store[i][j] = store[i][j - 1] + 1
        #             elif j == 0:
        #                 store[i][j] = store[i - 1][j] + 1
        #             else:
        #                 store[i][j] = min(store[i][j - 1] + 1, store[i - 1][j] + 1)
        # if waterCount == 0 or waterCount == m * n:
        #     return -1
        # res = 0
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if grid[i][j] == 0:
        #             if i == m - 1 and j == m - 1:
        #                 store[i][j] = min(m + n - 2, store[i][j])
        #             elif i == m - 1:
        #                 store[i][j] = min(store[i][j + 1] + 1, store[i][j])
        #             elif j == n - 1:
        #                 store[i][j] = min(store[i + 1][j] + 1, store[i][j])
        #             else:
        #                 store[i][j] = min(store[i][j + 1] + 1, store[i + 1][j] + 1, store[i][j])
        #             if res < store[i][j]:
        #                 res = store[i][j]
        # return res



sol = Solution()
# ans = sol.maxDistance([[1,0,1],[0,0,0],[1,0,1]])
# print(ans)
ans = sol.maxDistance([[1,0,0],[0,0,0],[0,0,0]])
print(ans)
# 「离陆地区域最远」要求海洋区域距离它最近的陆地区域的曼哈顿距离是最大的。