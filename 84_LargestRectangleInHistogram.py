'''
84. Largest Rectangle in Histogram
Hard

https://leetcode.com/problems/largest-rectangle-in-histogram/
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
'''
class Solution:
    def largestRectangleArea(self, heights) -> int:
        # # 方法一 左右扫描法
        # if len(heights) == 0:
        #     return 0
        # elif len(heights) == 1:
        #     return heights[0]
        # n = len(heights)
        #
        # left = [0] * n
        # right = [0] * n
        #
        # # 向右延伸
        # right[n - 1] = 1
        # for i in range(n - 2, -1, -1):
        #     if heights[i] > heights[i + 1]:
        #         right[i] = 1
        #     else:
        #         j = i + 1
        #         while j < n and heights[j] >= heights[i]:
        #             j += right[j]
        #         right[i] = j - i
        #
        # # 向左延伸
        # left[0] = 1
        # for i in range(1, n):
        #     if heights[i] > heights[i - 1]:
        #         left[i] = 1
        #     else:
        #         j = i - 1
        #         while j >= 0 and heights[j] >= heights[i]:
        #             j -= left[j]
        #         left[i] = i - j
        #
        # # 求面积
        # maxArea = heights[0]
        # for i in range(n):
        #     maxArea = max(heights[i] * (left[i] + right[i] - 1), maxArea)
        #
        # return maxArea


        # 方法二 辅助栈法
        heights.append(0)
        stack = []
        n = len(heights)
        maxArea = 0
        for i in range(n):
            if stack==[] or heights[stack[-1]] < heights[i]:
                stack.append(i)
            else:
                while stack!=[] and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    w = i if stack==[] else i-(stack[-1]+1)
                    maxArea = max(maxArea, h*w)
                stack.append(i)
        return maxArea

        


sol = Solution()
ans = sol.largestRectangleArea([2,1,5,6,2,3])
print(ans)
# 参考网址：https://www.cnblogs.com/boring09/p/4231906.html(程序有bug)
# 有两种方法，左右扫描或辅助栈。
# 方法I： 左右扫描法
# 考虑到最大面积的矩形高度一定跟某个条一样高（该条是最矮的），所以挨个枚举每个条，看其向左、向右最多能延伸到多远。# 在计算左右边界时，可以借助之前计算过的结果迭代（类似动归的感觉）优化以减少时间复杂度，这应该算是唯一的难点了。
# 方法II： 辅助栈法（网上很多人采用的方法）
# 根本思想是：依次遍历所有矩形条，尝试计算以该矩形条为高度的矩形面积。但是在遍历的时候我们不知道后面还有什么样的矩形条怎么办？没关系，对于没法确定面积的矩形，压栈，留着以后处理，而对于那些已经可以确定计算出面积的矩形条，留着也没用，弹栈。
# 我们怎么知道向左向右能延伸多远？观察下面几种情况：
# 情况1，第i个矩形比右边相邻的第i+1个矩形高，意味着，右边界不能更右了（废话），也不会在左边（向左只会让矩形面积减小）。所以在这种情况下，我们可以立即确定以第i个矩形的高度height[i]为高度的最大矩形面积的右边界。情况2，左边界同理。
# 如果当前矩形条的高度高于栈顶的矩形条的高度，对应情况2，得出，当前矩形一定是以它为高的矩形的左边界。
# 如果当前矩形条的高度小于或等于栈顶矩形条的高度，对应情况1，得出：栈顶的矩形一定是以它为高的矩形的右边界,所以可得以栈顶的矩形条高度为高度的最大矩形的面积！所以，可以放心把它删掉，或者说合并。
