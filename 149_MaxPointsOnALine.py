'''
149. Max Points on a Line
Hard

https://leetcode.com/problems/max-points-on-a-line/
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
'''
from math import sqrt
import numpy as np
# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        # 别人的程序
        n = len(points)
        slope_map = {}
        result = 0
        for i in range(n):

            slope_map.clear()      # 删除字典内所有元素 每次循环都清空 防止出现斜率相同截距不同的情况
            same, vertical = 1, 0
            slope_max = 0
            for j in range(i + 1, n):
                dx, dy = points[i].x - points[j].x, points[i].y - points[j].y
                if dx == dy == 0:  # 同一个点
                    same += 1
                elif dx == 0:  # 斜率无限大，垂直  注意此处为elif
                    vertical += 1
                else:
                    slope = (dy * np.longdouble(1)) / dx      # 斜率 对于斜率很靠近的线，python的计算精度不够。我们可以使用numpy模块或将dx转换成Decimal
                    # slope = float(dy) / float(dx)
                    slope_map[slope] = slope_map.get(slope, 0) + 1  # 即有则加1，无则设为1
                    slope_max = max(slope_max, slope_map[slope])
            result = max(result, max(slope_max, vertical) + same)  # 需要比较有斜率的个数和斜率不存在（垂直）的个数
            print(slope_map)
        return result

sol = Solution()
# count = sol.maxPoints([[1,1],[2,2],[3,3],[2,1],[2,3],[2,4],[2,5]])
# print(count)
# count = sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
# print(count)
# count = sol.maxPoints([[0,0]])
# print(count)
points = [Point(0,0),Point(1,1),Point(2,2),Point(2,1),Point(0,0)]
# points = [[0,0],[1,1],[2,2],[2,1],[0,0]]
count = sol.maxPoints(points)
print(count)


# 注意：考虑无值、零值、多值、重复值
# 测试集[[0,0],[94911151,94911150],[94911152,94911151]]，由于数字大，直接内置除法斜率会算成一样的，用numpy库运算
